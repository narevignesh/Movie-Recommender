```markdown
# 🎬 Movie Recommender System 🎥
content based recommender

Discover movies you'll love with the **Movie Recommender System**! This project uses machine learning techniques to provide personalized movie recommendations based on user input.

## 🌟 Features
- **Search Functionality:** Type or select your favorite movie to get similar movie recommendations.
- **Personalized Recommendations:** Provides a list of top 5 movies based on cosine similarity.
- **Interactive UI:** Built using Streamlit for a clean and responsive user interface.
- **Movie Details:** Recommendations include details like director, hero, and release year.

## 🚀 Live Demo
Check out the live demo of the application here:  
👉 [Movie Recommender System](https://movie-recommender-5o2w.onrender.com)

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **Backend:** Python
- **Machine Learning Libraries:** 
  - Scikit-learn
  - Pandas
  - NumPy
- **Data Processing:** Cosine similarity and CountVectorizer
- **Deployment:** Render

## 📚 How It Works
1. **Data Preprocessing:** 
   - Datasets from TMDB are merged and processed to extract meaningful tags for each movie.
   - Tags include genres, keywords, cast, and director names.
2. **Feature Engineering:**
   - A combined `tags` column is vectorized using `CountVectorizer`.
   - Cosine similarity is calculated for movie comparisons.
3. **Recommendation System:**
   - The user selects a movie, and the system recommends the top 5 similar movies.
```markdown
## 🖥️ Running the Project Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/narevignesh/Movie-Recommender.git
   cd Movie-Recommender
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```
4. Open your browser at `http://localhost:8501`.

## 📂 Project Structure
```
Movie-Recommender/
├── app.py               # Main application file
├── compress_similarity.py  # Script for handling large similarity matrices
├── recommend.py         # Recommendation logic
├── tmdb_5000_movies.csv # Movies dataset
├── tmdb_5000_credits.csv # Credits dataset
├── similarity.pkl       # Precomputed similarity matrix
├── movie_list.pkl       # Processed movie list
├── requirements.txt     # Required Python libraries
└── README.md            # Project documentation
```

## 📊 Dataset
The dataset used in this project is sourced from **TMDB (The Movie Database)** and includes details like:
- Movie title
- Overview
- Genres
- Keywords
- Cast and crew details

## 📝 Acknowledgements
- Datasets provided by **TMDB**.
- Frameworks and libraries used in this project: Streamlit, Pandas, Scikit-learn, and NumPy.

## ❤️ Contribution
Contributions are welcome! Feel free to submit a pull request or raise an issue for improvements.

---

### Author
**Vignesh**  
Connect with me on [GitHub](https://github.com/narevignesh)  

---
```

Let me know if you need any additional edits!


