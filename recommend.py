<<<<<<< HEAD
import pandas as pd

def recommend(movie, movies, similarity):
    """
    Recommend movies based on similarity.

    Args:
        movie (str): The title of the selected movie.
        movies (pd.DataFrame): DataFrame containing movie details.
        similarity (numpy.ndarray): Cosine similarity matrix.

    Returns:
        list[dict]: A list of dictionaries with recommended movie details.
    """
    try:
        # Get the index of the selected movie
        index = movies[movies['title'] == movie].index[0]
    except IndexError:
        raise ValueError(f"Movie '{movie}' not found in the dataset.")

    # Compute similarity scores and sort them
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    # Gather recommended movie details
    recommendations = []
    for i in distances[1:6]:  # Skip the first result (itself)
        recommended_movie = movies.iloc[i[0]]
        recommendations.append({
            'title': recommended_movie['title'],
            'director': recommended_movie['director'],
            'release_date': recommended_movie['release_date'],
            'hero': recommended_movie['hero'],
        })

    return recommendations
=======
import pandas as pd

def recommend(movie, movies, similarity):
    """
    Recommend movies based on similarity.

    Args:
        movie (str): The title of the selected movie.
        movies (pd.DataFrame): DataFrame containing movie details.
        similarity (numpy.ndarray): Cosine similarity matrix.

    Returns:
        list[dict]: A list of dictionaries with recommended movie details.
    """
    try:
        # Get the index of the selected movie
        index = movies[movies['title'] == movie].index[0]
    except IndexError:
        raise ValueError(f"Movie '{movie}' not found in the dataset.")

    # Compute similarity scores and sort them
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    # Gather recommended movie details
    recommendations = []
    for i in distances[1:6]:  # Skip the first result (itself)
        recommended_movie = movies.iloc[i[0]]
        recommendations.append({
            'title': recommended_movie['title'],
            'director': recommended_movie['director'],
            'release_date': recommended_movie['release_date'],
            'hero': recommended_movie['hero'],
        })

    return recommendations
>>>>>>> fee83ef29ef5bc7982a935e5c7f8cbac9b8c6923
