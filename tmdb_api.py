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
            "language": "tr-TR"
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        return None




'''
class TMDB:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.themoviedb.org/3"

    def get_popular_movies(self, genre_id=None, page=1):
        url = f"{self.base_url}/movie/popular"
        params = {
            'api_key': self.api_key,
            'page': page
        }
        if genre_id:
            params['with_genres'] = genre_id

        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        return None

    def get_movies_by_genre(self, genre_id, page=1):
        url = f"{self.base_url}/discover/movie"
        params = {
            'api_key': self.api_key,
            'with_genres': genre_id,
            'sort_by': 'popularity.desc',
            'page': page
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        return None

    def get_movie_details(self, movie_id):
        url = f"{self.base_url}/movie/{movie_id}"
        params = {'api_key': self.api_key}

        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        return None


    def get_movie_credits(self, movie_id):
        url = f"{self.base_url}/movie/{movie_id}/credits"
        params = {'api_key': self.api_key}

        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        return None '''