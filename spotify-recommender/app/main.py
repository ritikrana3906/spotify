from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.model.recommender import SongRecommender
import random

app = FastAPI()

# Initialize the SongRecommender
recommender = SongRecommender()

class RecommendRequest(BaseModel):
    index: int
    n_recommendations: int = 5  # Default to 5

@app.get('/list_songs')
def list_songs(limit: int = 10):
    # Randomly select 5 indices
    random_indices = random.sample(range(len(recommender.songs)), 5)
    print(f"Random Indices: {random_indices}")  # This will print random indices to the console
    return recommender.list_songs(limit)


@app.get('/')
def home():
    return {"message": "Welcome to Spotify KNN Recommender API"}

@app.post('/recommend')
def recommend_song(request: RecommendRequest):
    """
    Recommends songs based on the song index and number of recommendations.
    """
    recommended_songs = recommender.recommend(request.index, request.n_recommendations)
    return recommended_songs

@app.get('/list_songs')
def list_songs(limit: int = 10):
    """
    Lists a certain number of songs from the dataset.
    """
    return recommender.list_songs(limit)

@app.get('/song_info/{index}')
def song_info(index: int):
    """
    Retrieves details about a specific song by its index.
    """
    song = recommender.get_song_info(index)
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")
    return song
 
 