import streamlit as st
import pickle
import pandas as pd
import requests

movie_dict = pickle.load(open('recommend_movie.pkl','rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

def poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    dist = similarity[movie_index]
    movie_list = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:11]

    recommended = []
    movie_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        movie_poster.append(poster(movie_id))
        recommended.append(movies.iloc[i[0]].title)
    return recommended, movie_poster


st.title("Movie Recommender System")

selected_movie = st.selectbox('Choose a movie',movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movie)

    col1,col2,col3,col4,col5 = st.columns(5)

    with col1:
        st.image(posters[0])
        st.text(names[0])

    with col2:
        st.image(posters[1])
        st.text(names[1])

    with col3:
        st.image(posters[2])
        st.text(names[2])

    with col4:
        st.image(posters[3])
        st.text(names[3])

    with col5:
        st.image(posters[4])
        st.text(names[4])

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(posters[5])
        st.text(names[5])

    with col2:
        st.image(posters[6])
        st.text(names[6])

    with col3:
        st.image(posters[7])
        st.text(names[7])

    with col4:
        st.image(posters[8])
        st.text(names[8])

    with col5:
        st.image(posters[9])
        st.text(names[9])

