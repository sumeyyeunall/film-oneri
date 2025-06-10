# Mood-Based Movie Recommendation App

This project is a Streamlit-based web application that recommends movies based on your current mood. It uses AI-powered sentiment analysis and the TMDB API to suggest movies matching your feelings.

## Features
- **Sentiment Analysis:** Uses a pre-trained transformer model to analyze your mood from text input.
- **Mood to Genre Mapping:** Matches moods like Positive, Negative, and Neutral to specific movie genres.
- **Movie Recommendations:** Fetches popular movies from TMDB based on your mood.
- **Movie Details:** View detailed information about the recommended movies, including cast, runtime, and overview.

## How It Works
1. You type how you feel in the input box.
2. The app analyzes your text using the `transformers` sentiment analysis pipeline.
3. Based on the detected mood (Positive, Negative, or Neutral), it maps to predefined movie genres.
4. It fetches popular movies of those genres from the TMDB API.
5. You get a list of movie suggestions with posters and basic info.
6. Click "Show Details" to see more about any movie.
7. 
## Note on Neutral Mood
The underlying sentiment model only detects Positive and Negative sentiments. Neutral mood is inferred based on the confidence score threshold (below 0.75). This heuristic may not be perfect, and improvements can be made by using a multi-class sentiment model.



