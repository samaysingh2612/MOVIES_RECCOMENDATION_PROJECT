import requests

API_KEY = "9daf59e67bb1b2479317ad892498b251"

def fetch_poster(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"

    data = requests.get(url).json()

    poster_path = data["poster_path"]

    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path

    return full_path