import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        #
        # movie_id = i[0]
        # fetch poster from API
        
        #
        recommended_movies.append(movies.iloc[i[0]].title)
    
    return recommended_movies


# movies_list = pickle.load(open('movies.pkl', 'rb'))
# movies_list = movies_list['title'].values 

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))
 
st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Please Select a movie',
                       movies['title'].values)


if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
         
         
         
         
         
         





# import streamlit as st
# import pandas as pd
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.feature_extraction.text import CountVectorizer

# # load dataset
# movies = pd.read_csv('tmdb_5000_movies.csv')

# # simple preprocessing (you may already have this in notebook)
# movies = movies[['title', 'overview']]
# movies.dropna(inplace=True)

# # create tags
# movies['tags'] = movies['overview']

# # vectorization
# cv = CountVectorizer(max_features=5000, stop_words='english')
# vectors = cv.fit_transform(movies['tags']).toarray()

# # similarity
# similarity = cosine_similarity(vectors)


# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)),
#                          reverse=True,
#                          key=lambda x: x[1])[1:6]

#     recommended_movies = []
#     for i in movies_list:
#         recommended_movies.append(movies.iloc[i[0]].title)

#     return recommended_movies


# st.title('Movie Recommender System')

# selected_movie_name = st.selectbox(
#     'Select a movie',
#     movies['title'].values
# )

# if st.button('Recommend'):
#     recommendations = recommend(selected_movie_name)
#     for i in recommendations:
#         st.write(i)