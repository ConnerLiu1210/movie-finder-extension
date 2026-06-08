import os
import requests

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")


@app.get("/")
def home():
    return {"message": "SafeWatch backend is running"}


@app.get("/search")
def search(title: str):
    search_url = "https://api.themoviedb.org/3/search/movie"

    search_params = {
    "api_key": TMDB_API_KEY,
    "query": title,
    "language": "zh-CN"
}

    search_response = requests.get(search_url, params=search_params)
    search_data = search_response.json()

    if not search_data.get("results"):
        return {"error": "Movie not found"}

    movie = search_data["results"][0]
    movie_id = movie.get("id")

    providers_url = f"https://api.themoviedb.org/3/movie/{movie_id}/watch/providers"
    providers_response = requests.get(
    providers_url,
    params={
        "api_key": TMDB_API_KEY,
        "language": "zh-CN"
    }
)
    providers_data = providers_response.json()

    us_data = providers_data.get("results", {}).get("US", {})

    watch_link = us_data.get("link")

    providers = []

    for category in ["flatrate", "rent", "buy"]:
        for item in us_data.get(category, []):
            providers.append({
    "name": item.get("provider_name"),
    "type": category,
    "logo": (
        f"https://image.tmdb.org/t/p/w92{item.get('logo_path')}"
        if item.get("logo_path")
        else None
    )
})

    return {
        "title": movie.get("title"),
        "year": movie.get("release_date", "")[:4],
        "overview": movie.get("overview"),
        "tmdb_id": movie_id,
        "poster": (
            f"https://image.tmdb.org/t/p/w500{movie.get('poster_path')}"
            if movie.get("poster_path")
            else None
        ),
        "watch_link": watch_link,
        "providers": providers
    }