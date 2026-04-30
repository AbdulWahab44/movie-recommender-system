# 🎬 Movie Recommender System (Content-Based Filtering)

---

## 📌 Overview
This project is a **Content-Based Movie Recommender System** built using machine learning techniques. It recommends movies based on their similarity to a selected movie by analyzing content features such as descriptions, cast, keywords, and other metadata.

The system is developed using a dataset from **Kaggle** and provides an interactive user experience through a **Streamlit web application**.

---

## 📊 Data Collection
The dataset used in this project is sourced from Kaggle and contains detailed information about movies, including:

- 🎞 Movie titles  
- 📝 Descriptions / overviews  
- 🎭 Cast and crew information  
- 🔑 Keywords and related metadata  

📌 Dataset Source: Kaggle Movie Dataset

---

## ⚙️ Data Preprocessing
Several preprocessing steps were performed to prepare the data for modeling:

- Handled missing and inconsistent values  
- Cleaned and structured raw dataset  
- Combined important features into a single representation (tags)  
- Applied feature weighting to improve recommendation quality  

---

## 🧠 Implementation
The recommender system is based on **Content-Based Filtering**:

- Movies are converted into text-based feature representations  
- Text data is transformed into numerical vectors using **Bag of Words (BOW) / CountVectorizer**  
- Similarity between movies is calculated using **Cosine Similarity**  
- The system returns the most similar movies based on user selection  

---

## 💻 Front-End Interface
A simple and interactive interface is built using **Streamlit**:

- Users can select a movie from a dropdown list  
- Click on the **Recommend** button  
- The system displays a list of similar movies instantly  

The application is also deployed for easy access.

---

## 🚀 How to Run

1️⃣ Clone the repository:
```bash
git clone https://github.com/AbdulWahab44/100-days-of-machine-learning/tree/main/ML-Projects/movie-recommender-system.git
cd movie-recommender-system