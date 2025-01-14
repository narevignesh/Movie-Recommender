import streamlit as st
import pickle

# Set up the page configuration
st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎥",
    layout="wide",
)

# App header
st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="color: #FF4B4B;">🎬 Movie Recommender System 🎬</h1>
        <p style="font-size: 16px;">Discover movies you'll love! Enter your favorite movie to get personalized recommendations.</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# Load data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Dropdown for movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list,
    index=0,
    help="Search for your favorite movie to get recommendations."
)

def recommend(movie, movies, similarity):
    """Recommend movies based on similarity."""
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommendations = []
    for i in distances[1:6]:  # Fetch top 5 recommendations
        recommended_movie = movies.iloc[i[0]]
        recommendations.append({
            'title': recommended_movie['title'],
            'director': recommended_movie['director'],
            'release_date': recommended_movie['release_date'],
            'hero': recommended_movie['hero'],
        })
    
    return recommendations

# Show recommendations
if st.button('Show Recommendations', use_container_width=True):
    recommendations = recommend(selected_movie, movies, similarity)
    
    # Display recommendations as styled cards
    for rec in recommendations:
        st.markdown(
            f"""
            <div style="border: 2px solid #FF4B4B; border-radius: 15px; padding: 20px; margin-bottom: 20px; background-color: #FFF3F3;">
                <h3 style="color: #FF4B4B;">🎥 {rec['title']}</h3>
                <p><strong>Director:</strong> {rec['director']}</p>
                <p><strong>Hero:</strong> {rec['hero']}</p>
                <p><strong>Release Year:</strong> {rec['release_date']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# Footer (Stick it to the bottom)
st.markdown(
    """
    <div style="position: fixed; left: 0; bottom: 0; width: 100%; background-color: #FFF3F3; text-align: center; padding: 10px 0;">
        <hr style="border: 1px solid #FF4B4B;">
        <footer style="font-size: 14px; color: #FF4B4B;">
            Built with ❤️ using Streamlit | By VIGNESH
        </footer>
    </div>
    """, 
    unsafe_allow_html=True
)
