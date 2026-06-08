# 🎬 Movie Finder Extension

A Chrome extension that helps users discover where movies and TV shows are legally available to watch.

## Features

- Search for movies and TV shows by title
- Retrieve real-time movie information using TMDB API
- Display movie poster, release year, and overview
- Show available streaming providers
- Provide official watch links
- Lightweight and easy-to-use Chrome extension

## Demo

Search for a movie title such as:

text Interstellar Titanic Inception 

The extension displays:

- Movie title
- Release year
- Poster
- Overview
- Streaming providers
- Official viewing options

## Tech Stack

### Frontend

- Chrome Extension (Manifest V3)
- HTML
- CSS
- JavaScript

### Backend

- Python
- FastAPI
- Requests

### APIs

- TMDB API
- TMDB Watch Providers

## Project Structure

text movie-finder-extension/ │ ├── backend/ │   ├── main.py │   ├── requirements.txt │   └── .env │ ├── extension/ │   ├── manifest.json │   ├── popup.html │   ├── popup.css │   └── popup.js │ └── README.md 

## Installation

### Clone Repository

bash git clone https://github.com/ConnerLiu1210/movie-finder-extension.git 

### Install Dependencies

bash cd backend pip install -r requirements.txt 

### Configure Environment Variables

Create a .env file inside the backend directory:

env TMDB_API_KEY=YOUR_API_KEY 

### Run Backend

bash uvicorn main:app --reload --port 8000 

### Load Chrome Extension

1. Open Chrome
2. Navigate to:

text chrome://extensions 

3. Enable Developer Mode
4. Click Load unpacked
5. Select the extension folder

## Future Improvements

- Direct streaming platform links
- Watchlist support
- Search history
- Personalized recommendations
- AI-powered movie recommendations
- Cloud deployment
- Chrome Web Store release

## Disclaimer

This project only provides information about legal streaming availability and does not host, distribute, or provide copyrighted content.

## Author

Conner Liu  
The Ohio State University  
Computer Science and Engineering
