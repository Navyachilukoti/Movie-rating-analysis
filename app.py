import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from movie_rating import MovieRatingSystem

# Set page config
st.set_page_config(
    page_title="IMDb Movies India Analysis",
    page_icon="🎬",
    layout="wide"
)

# Title and description
st.title("🎬 IMDb Movies India Analysis")
st.markdown("""
This interactive dashboard provides insights and analysis of Indian movies from IMDb.
Explore ratings, genres, and trends in Indian cinema.
""")

# Initialize the movie rating system
@st.cache_data
def load_data():
    rating_system = MovieRatingSystem()
    rating_system.load_dataset('IMDb Movies India.csv')
    return rating_system

try:
    rating_system = load_data()
    df = rating_system.df

    # Sidebar filters
    st.sidebar.header("Filters")
    selected_genre = st.sidebar.multiselect(
        "Select Genres",
        options=sorted(df['Genre'].unique()),
        default=[]
    )

    year_range = st.sidebar.slider(
        "Select Year Range",
        min_value=int(df['Year'].min()),
        max_value=int(df['Year'].max()),
        value=(int(df['Year'].min()), int(df['Year'].max()))
    )

    # Filter data based on selections
    filtered_df = df.copy()
    if selected_genre:
        filtered_df = filtered_df[filtered_df['Genre'].isin(selected_genre)]
    filtered_df = filtered_df[
        (filtered_df['Year'] >= year_range[0]) & 
        (filtered_df['Year'] <= year_range[1])
    ]

    # Main content
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Movies", len(filtered_df))
    with col2:
        st.metric("Average Rating", f"{filtered_df['Rating'].mean():.2f}")
    with col3:
        st.metric("Highest Rated", f"{filtered_df['Rating'].max():.2f}")
    with col4:
        st.metric("Most Votes", f"{filtered_df['Votes'].max():,.0f}")

    # Top Movies
    st.header("Top Rated Movies")
    top_movies = filtered_df.nlargest(10, 'Rating')[['Name', 'Rating', 'Votes', 'Genre']]
    st.dataframe(top_movies, use_container_width=True)

    # Genre Distribution
    st.header("Genre Distribution")
    genre_counts = filtered_df['Genre'].value_counts().head(10)
    fig_genre = px.bar(
        x=genre_counts.index,
        y=genre_counts.values,
        title="Top 10 Genres"
    )
    st.plotly_chart(fig_genre, use_container_width=True)

    # Year-wise Analysis
    st.header("Movies by Year")
    year_counts = filtered_df['Year'].value_counts().sort_index()
    fig_year = px.line(
        x=year_counts.index,
        y=year_counts.values,
        title="Number of Movies Released Each Year"
    )
    st.plotly_chart(fig_year, use_container_width=True)

    # Rating Distribution
    st.header("Rating Distribution")
    fig_rating = px.histogram(
        filtered_df,
        x='Rating',
        nbins=20,
        title="Distribution of Movie Ratings"
    )
    st.plotly_chart(fig_rating, use_container_width=True)

    # Search functionality
    st.header("Search Movies")
    search_term = st.text_input("Enter movie name or director")
    if search_term:
        search_results = filtered_df[
            filtered_df['Name'].str.contains(search_term, case=False, na=False) |
            filtered_df['Director'].str.contains(search_term, case=False, na=False)
        ]
        if not search_results.empty:
            st.dataframe(search_results[['Name', 'Year', 'Rating', 'Genre', 'Director']], use_container_width=True)
        else:
            st.info("No movies found matching your search.")

except Exception as e:
    st.error(f"Error loading data: {str(e)}")
    st.info("Please make sure the 'IMDb Movies India.csv' file is in the same directory as this app.") 