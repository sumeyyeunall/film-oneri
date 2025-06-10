import requests
import streamlit as st

def show_movie_details(movie_id):
    api_key = "242aad67fc75bd3d0fc6a785837d4c28"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        movie = response.json()
        st.markdown(f"## {movie['title']}")
        st.write(f"🗓 Release Date: {movie.get('release_date', 'Unknown')}")
        st.write(f"🎬 Genres: {', '.join([genre['name'] for genre in movie.get('genres', [])])}")
        st.write(f"📄 Overview:\n{movie.get('overview', 'Not available')}")
        st.image(f"https://image.tmdb.org/t/p/w500{movie['poster_path']}")
    else:
        st.error("Failed to fetch movie details.")