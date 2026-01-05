# 🎬 Movie Recommender System 🎥  
**Content-Based Recommender**

Discover movies you'll love with the **Movie Recommender System**. This project uses machine learning techniques to provide personalized movie recommendations based on user input.

## 🌟 Features
- **Search Functionality:** Type or select your favorite movie to get similar movie recommendations.
- **Personalized Recommendations:** Displays the top 5 movies using cosine similarity.
- **Interactive UI:** Built with Streamlit for a clean and responsive interface.
- **Movie Details:** Includes director, lead actor, and release year.

## 🚀 Live Demo
👉 [Movie Recommender System](https://movie-recommender-5o2w.onrender.com)

## 🛠️ Tech Stack
- **Frontend:** Streamlit  
- **Backend:** Python  
- **Machine Learning:**  
  - Scikit-learn  
  - Pandas  
  - NumPy  
- **Techniques:** CountVectorizer, Cosine Similarity  
- **Deployment:** Render  

## 📚 How It Works
1. **Data Preprocessing**
   - TMDB datasets are merged and cleaned.
   - Tags are created using genres, keywords, cast, and director.
2. **Feature Engineering**
   - Tags are vectorized using `CountVectorizer`.
   - Cosine similarity is computed between movies.
3. **Recommendation**
   - Based on the selected movie, the top 5 most similar movies are recommended.
