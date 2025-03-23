# IMDb Movies India Analysis

This project analyzes the IMDb Movies India dataset to provide insights about Indian movies, their ratings, genres, and other statistics.

## Features

- Load and process IMDb Movies India dataset
- Calculate basic statistics (total movies, average rating)
- Find highest rated and most voted movies
- Analyze movie genres
- Display top rated movies
- Year-wise movie analysis

## Requirements

- Python 3.x
- pandas
- numpy

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Navyachilukoti/movie-rating-analysis.git
cd movie-rating-analysis
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Download the dataset:
   - The IMDb Movies India dataset can be downloaded from [Kaggle](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows)
   - Place the downloaded `IMDb Movies India.csv` file in the project root directory

## Usage

Run the project using either of these commands:

```bash
python3 movie_rating.py
```
or
```bash
./run.sh
```

## Dataset Description

The IMDb Movies India dataset contains information about Indian movies from IMDb. The dataset includes the following columns:

- **Name**: Title of the movie
- **Year**: Release year of the movie
- **Duration**: Length of the movie in minutes
- **Genre**: Movie genre(s)
- **Rating**: IMDb rating (out of 10)
- **Votes**: Number of votes received
- **Director**: Movie director
- **Actor 1**: Lead actor/actress
- **Actor 2**: Supporting actor/actress
- **Actor 3**: Supporting actor/actress
- **Actor 4**: Supporting actor/actress
- **Description**: Brief plot description

### Dataset Statistics
- Total number of movies: 15,509
- Average rating: 5.84/10
- Most common genre: Drama (2,780 movies)
- Most voted movie: Life of Pi (591,417 votes)

## Output

The program provides:
1. Dataset Statistics
   - Total number of movies
   - Average rating
   - Highest rated movie
   - Most voted movie
2. Genre Analysis
   - Top 5 genres by movie count
   - Genre distribution
3. Year-wise Analysis
   - Top 5 years by movie count
4. Top 10 Rated Movies
   - Movie name
   - Rating
   - Number of votes
   - Genre

## Project Structure

```
movie-rating-analysis/
├── movie_rating.py      # Main Python script
├── run.sh              # Shell script to run the project
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── LICENSE            # MIT License
└── IMDb Movies India.csv  # Dataset file (not included in repository)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - See LICENSE file for details 