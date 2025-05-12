import streamlit as st
import pandas as pd
import pickle
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env into environment

API_KEY = os.getenv("API_KEY")  

def download_from_gdrive(file_id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()
    response = session.get(URL, params={'id': file_id}, stream=True)

    # Check for warning token
    def get_confirm_token(resp):
        for key, value in resp.cookies.items():
            if key.startswith('download_warning'):
                return value
        return None

    token = get_confirm_token(response)

    if token:
        response = session.get(URL, params={'id': file_id, 'confirm': token}, stream=True)

    # Write file
    with open(destination, "wb") as f:
        for chunk in response.iter_content(32768):
            if chunk:
                f.write(chunk)

# Replace with your actual file ID and destination filename
download_from_gdrive("1ahiS04efmIFmitL9QxwQbrYTbnl_JW8u", "similarity.pkl")

# --- Function to fetch poster
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        if data.get("poster_path"):
            return "https://image.tmdb.org/t/p/w500" + data["poster_path"]
    except Exception as e:
        print(f"Error fetching poster: {e}")
    return None

# --- Recommendation logic (case-insensitive title matching + loader support)
def recommendation(title, data):
    normalized_title = title.strip().lower()
    data['normalized_title'] = data['TITLE'].str.strip().str.lower()

    if normalized_title not in data['normalized_title'].values:
        return []

    movie_index = data[data['normalized_title'] == normalized_title].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    for i in movies_list:
        movie_id = data.iloc[i[0]].FILMID
        movie_title = data.iloc[i[0]].TITLE
        poster_url = fetch_poster(movie_id)
        recommended_movies.append((movie_title, poster_url))
    
    return recommended_movies

# --- Load data
data = pd.read_csv('data.csv')
with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

# --- Streamlit UI
st.title('🎬 Movie Recommender')

selected_movie = st.selectbox(
    'Enter or select a movie you have seen before to get recommendations:',
    data['TITLE'].values
)

if st.button('Recommend'):
    with st.spinner('Finding your next binge-worthy picks... 🔍'):
        results = recommendation(selected_movie, data)

        if not results:
            st.error("Movie not currently in the database. Try another one?")
        else:
            cols = st.columns(5)
            for idx, (name, poster) in enumerate(results):
                with cols[idx % 5]:
                    if poster:
                        st.image(poster, use_container_width=True)
                    st.caption(name)
