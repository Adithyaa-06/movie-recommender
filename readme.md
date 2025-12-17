# 🎬 Movie Recommender System

A high-performance, content-based movie recommendation engine built with **Python**, **Machine Learning**, and **Streamlit**. This application suggests the top 5 similar movies based on a user's selection, including high-quality posters fetched via the TMDb API.

## 🚀 Features
* **Interactive UI:** Clean dropdown menu for easy movie selection.
* **Real-time Posters:** Dynamically fetches movie posters using the TMDb API.
* **Instant Recommendations:** Powered by a pre-computed Similarity Matrix (Cosine Similarity) for zero-lag results.

## 🧠 How it Works
1. **Data Preprocessing:** Movie metadata (genres, keywords, cast, and crew) is merged to create a "tags" column.
2. **Vectorization:** Tags are converted into numerical vectors using **CountVectorizer** (Bag of Words).
3. **Similarity Calculation:** **Cosine Similarity** is calculated between all movie vectors to determine how "close" movies are to each other.
4. **Serialization:** The final model and similarity matrix are exported as `.pkl` files using Pickle for use in the web app.



## 🛠️ Tech Stack
* **Language:** Python
* **UI/Framework:** Streamlit
* **Machine Learning:** Scikit-Learn
* **Data Processing:** Pandas, Numpy
* **API:** The Movie Database (TMDb)
* **Version Control:** Git LFS (for large model files)

## 📂 Project Structure
```text
├── artifacts/            # Pickled model files (similarity.pkl, movie_list.pkl)
├── docs/                 # Project documentation and presentations
├── app.py                # Main Streamlit web application
├── movie.py              # Jupyter/Python script for model building
├── requirements.txt      # Python dependencies
└── .gitignore            # Files excluded from Git
