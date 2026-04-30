# 🎬 Movie Recommender System (Content-Based)

## 🚀 Overview

This project is a content-based movie recommender system that suggests similar movies based on user selection. It analyzes movie metadata such as cast, keywords, and descriptions to generate accurate recommendations.

---

## 🧠 Features

* Select a movie and get similar recommendations
* Fast similarity-based results using precomputed data
* Simple and interactive UI
* Deployed web application using Streamlit

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* NLP (Bag of Words / CountVectorizer)
* Streamlit

---

## ⚙️ How It Works

1. Load and clean the movie dataset
2. Combine important features into tags
3. Convert text data into vectors (BOW)
4. Compute similarity using cosine similarity
5. Recommend top similar movies

---

## 📊 Dataset

The dataset is sourced from Kaggle and includes:

* Movie titles
* Overviews
* Cast and crew
* Keywords

---

## 📦 Installation

```bash
git clone https://github.com/AbdulWahab44/movie-recommender-system.git
cd movie-recommender-system
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
movie-recommender-system/
│
├── app.py
├── requirements.txt
├── README.md
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
└── notebooks/
```

---

## 🌍 Future Improvements

* Add movie posters using TMDB API
* Improve recommendation accuracy
* Add search functionality
* Enhance UI (Netflix-style)

---

## 🤝 Contributing

Feel free to fork this repository and improve it.

---

## ⭐ Acknowledgment

Dataset provided by Kaggle. This project is built for learning and demonstrating recommendation systems.
