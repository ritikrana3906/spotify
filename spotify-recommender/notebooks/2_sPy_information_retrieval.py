import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
import pandas as pd

# Load client ID and secret from .env
load_dotenv('spotify-recommender/notebooks/details.env')

client_id=os.getenv("SPOTIFY_CLIENT_ID")
client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")

# Check if they are being read
if not client_id or not client_secret:
    print("❌ Client ID or Secret not found. Check your .env file.")
else:
    print("✅ Credentials loaded successfully")

# Set up authentication
try:
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    
    # Make a test call (get info about a known track)
    # test_track_id = "3n3Ppam7vgaVa1iaRUc9Lp"
    test_track_id = "spotify:track:0UaMYEvWZi0ZqiDOoHU3YI"  # Eminem - Lose Yourself
    track = sp.track(test_track_id)

    print("✅ Spotify API is working!")
    print(f"Track name: {track['name']}, Artist: {track['artists'][0]['name']}")

except Exception as e:
    print("❌ Spotify API connection failed:")
    print(e)

# Load the dataset
data_path = os.getenv("DATA_PATH")

df = pd.read_csv(data_path)
print(df.head(1))
track2 = sp.track(df['track_uri'][0])
print(track2)