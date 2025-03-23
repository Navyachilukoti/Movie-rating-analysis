import pandas as pd
import numpy as np

class MovieRatingSystem:
    def __init__(self):
        self.movies = {}  # Dictionary to store movie data
        self.ratings = {}  # Dictionary to store user ratings
        self.df = None  # DataFrame to store the dataset
        
    def load_dataset(self, file_path):
        """Load the IMDb Movies India dataset"""
        try:
            # Try different encodings
            encodings = ['utf-8', 'latin1', 'iso-8859-1']
            for encoding in encodings:
                try:
                    self.df = pd.read_csv(file_path, encoding=encoding)
                    print(f"Successfully loaded the dataset with {encoding} encoding")
                    break
                except UnicodeDecodeError:
                    continue
            
            if self.df is None:
                raise ValueError("Could not read the CSV file with any of the attempted encodings")
            
            # Clean the data
            self.df['Rating'] = pd.to_numeric(self.df['Rating'], errors='coerce')
            self.df['Votes'] = pd.to_numeric(self.df['Votes'].str.replace(',', ''), errors='coerce')
            
            # Add movies to the system
            for idx, row in self.df.iterrows():
                self.add_movie(idx, row['Name'], row['Genre'])
                
        except Exception as e:
            print(f"Error loading dataset: {str(e)}")
            raise
    
    def add_movie(self, movie_id, title, genre):
        """Add a new movie to the system"""
        self.movies[movie_id] = {
            'title': title,
            'genre': genre,
            'avg_rating': 0,
            'total_ratings': 0
        }
    
    def add_rating(self, user_id, movie_id, rating):
        """Add a user rating for a movie (rating should be 1-5)"""
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")
            
        if movie_id not in self.movies:
            raise ValueError("Movie not found")
            
        # Store the user rating
        if movie_id not in self.ratings:
            self.ratings[movie_id] = {}
        self.ratings[movie_id][user_id] = rating
        
        # Update average rating
        avg = sum(self.ratings[movie_id].values()) / len(self.ratings[movie_id])
        self.movies[movie_id]['avg_rating'] = round(avg, 2)
        self.movies[movie_id]['total_ratings'] = len(self.ratings[movie_id])
    
    def get_movie_rating(self, movie_id):
        """Get the average rating for a movie"""
        if movie_id not in self.movies:
            raise ValueError("Movie not found")
        return self.movies[movie_id]['avg_rating']
    
    def analyze_movies(self):
        """Analyze the movie dataset"""
        if self.df is None:
            raise ValueError("Dataset not loaded. Please load the dataset first.")
            
        # Basic statistics
        print("\nDataset Statistics:")
        print(f"Total number of movies: {len(self.df)}")
        print(f"Average rating: {self.df['Rating'].mean():.2f}")
        print(f"Highest rated movie: {self.df.loc[self.df['Rating'].idxmax(), 'Name']} ({self.df['Rating'].max():.2f})")
        print(f"Most voted movie: {self.df.loc[self.df['Votes'].idxmax(), 'Name']} ({self.df['Votes'].max():,} votes)")
        
        # Genre analysis
        print("\nTop 5 Genres:")
        genre_counts = self.df['Genre'].value_counts().head()
        for genre, count in genre_counts.items():
            print(f"{genre}: {count} movies")
            
        # Year analysis
        self.df['Year'] = pd.to_numeric(self.df['Year'], errors='coerce')
        print("\nMovies by Year (Top 5):")
        year_counts = self.df['Year'].value_counts().head()
        for year, count in year_counts.items():
            print(f"{year}: {count} movies")
    
    def get_top_rated_movies(self, n=10):
        """Get top n rated movies"""
        if self.df is None:
            raise ValueError("Dataset not loaded. Please load the dataset first.")
            
        top_movies = self.df.nlargest(n, 'Rating')[['Name', 'Rating', 'Votes', 'Genre']]
        return top_movies

# Example usage
if __name__ == "__main__":
    rating_system = MovieRatingSystem()
    
    # Load the dataset
    rating_system.load_dataset('IMDb Movies India.csv')
    
    # Analyze the movies
    rating_system.analyze_movies()
    
    # Get top rated movies
    print("\nTop 10 Rated Movies:")
    top_movies = rating_system.get_top_rated_movies(10)
    for _, movie in top_movies.iterrows():
        print(f"{movie['Name']}: {movie['Rating']:.2f} ({movie['Votes']:,} votes) - {movie['Genre']}")
