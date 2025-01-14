import pandas as pd
import ast
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

# Merge and preprocess data
movies = movies.merge(credits, on='title')
movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew', 'release_date']]
movies.dropna(inplace=True)

def convert(text):
    return [i['name'] for i in ast.literal_eval(text)]

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)

def fetch_director(text):
    directors = [i['name'] for i in ast.literal_eval(text) if i['job'] == 'Director']
    return directors[0] if directors else "Unknown"

movies['director'] = movies['crew'].apply(fetch_director)

def fetch_hero(cast_list):
    cast = [i['name'] for i in ast.literal_eval(cast_list)]
    return cast[0] if cast else "Unknown"

movies['hero'] = movies['cast'].apply(fetch_hero)
movies['cast'] = movies['cast'].apply(lambda x: [i['name'] for i in ast.literal_eval(x)][:3])

def collapse(L):
    return [i.replace(" ", "") for i in L]

movies['genres'] = movies['genres'].apply(collapse)
movies['keywords'] = movies['keywords'].apply(collapse)
movies['cast'] = movies['cast'].apply(collapse)
movies['overview'] = movies['overview'].apply(lambda x: x.split())

# Fix: Ensure row-wise concatenation of lists
movies['tags'] = movies.apply(
    lambda row: row['overview'] + row['genres'] + row['keywords'] + row['cast'] + [row['director']],
    axis=1
)

# Create a DataFrame with relevant columns
new = movies[['movie_id', 'title', 'tags', 'release_date', 'director', 'hero']].copy()
new['tags'] = movies['tags'].apply(lambda x: " ".join(x))

# Vectorize tags and compute similarity
cv = CountVectorizer(max_features=5000, stop_words='english')
vector = cv.fit_transform(new['tags']).toarray()
similarity = cosine_similarity(vector)

# Save processed data
pickle.dump(new, open('movie_list.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))
