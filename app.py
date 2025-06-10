import streamlit as st
from sentiment_analysis import SentimentAnalyzer
from tmdb_api import TMDBClient
from show_details import show_movie_details

st.set_page_config(page_title="Mood-Based Movie Recommender", layout="wide")
st.title("🎬 Mood-Based Movie Recommendation")

sentiment_analyzer = SentimentAnalyzer()
tmdb = TMDBClient(api_key="242aad67fc75bd3d0fc6a785837d4c28")  # Your TMDB API key here

# Mood → genre ID mapping
MOOD_GENRE_MAPPING = {
    'POSITIVE': {
        'genres': [35, 10749],  # Comedy, Romance
        'description': "You seem happy! We recommend comedies or romantic movies."
    },
    'NEGATIVE': {
        'genres': [18, 80],  # Drama, Crime
        'description': "Feeling a bit down? Drama and mystery movies might suit you."
    },
    'NEUTRAL': {
        'genres': [99, 9648],  # Documentary, Mystery
        'description': "Feeling neutral. Documentaries or thrillers are good choices."
    }
}

# Initialize session state
if 'movies' not in st.session_state:
    st.session_state.movies = []
if 'selected_movie_id' not in st.session_state:
    st.session_state.selected_movie_id = None
if 'sentiment' not in st.session_state:
    st.session_state.sentiment = None

# User input
user_input = st.text_area("🎭 How are you feeling today?", height=100, placeholder="Describe your mood in a few sentences...")

if st.button("🎲 Recommend a Movie"):
    if user_input.strip():
        result = sentiment_analyzer.analyze(user_input)
        sentiment = result['sentiment']
        confidence = result['confidence']

        st.session_state.sentiment = sentiment
        st.session_state.confidence = confidence

        mood_data = MOOD_GENRE_MAPPING.get(sentiment, MOOD_GENRE_MAPPING['NEUTRAL'])
        st.session_state.mood_data = mood_data

        # Fetch movies by genres
        st.session_state.movies = []
        for genre_id in mood_data['genres']:
            data = tmdb.get_popular_movies(genre_id=genre_id)
            if data and 'results' in data:
                st.session_state.movies.extend(data['results'])

# Display sentiment and movie suggestions
if st.session_state.sentiment:
    st.success(f"💡 Your Mood: `{st.session_state.sentiment}` (Confidence: {st.session_state.confidence * 100:.1f}%)")
    st.info(st.session_state.mood_data['description'])

    cols = st.columns(3)
    for idx, movie in enumerate(st.session_state.movies[:6]):
        with cols[idx % 3]:
            st.markdown(f"### 🎞 {movie['title']}")
            st.caption(f"Year: {movie.get('release_date', 'Unknown')}")
            st.caption(f"IMDB Rating: ⭐ {movie.get('vote_average', '?')}")
            poster = movie.get('poster_path')
            if poster:
                st.image(f"https://image.tmdb.org/t/p/w500{poster}", width=200)
            overview = movie.get('overview', '')
            st.write(overview[:180] + "..." if overview else "No description available.")
            if st.button(f"📖 Show Details - {movie['title']}", key=f"movie_{movie['id']}"):
                st.session_state.selected_movie_id = movie['id']

# Show selected movie details
if st.session_state.selected_movie_id:
    show_movie_details(st.session_state.selected_movie_id)
