import requests

class TMDBClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.themoviedb.org/3"

    def get_popular_movies(self, genre_id):
        url = f"{self.base_url}/discover/movie"
        params = {
            "api_key": self.api_key,
            "with_genres": genre_id,
            "sort_by": "popularity.desc",
            "language": "en-EN"
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        return None
