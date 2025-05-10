import requests

# Base URL of your API
BASE_URL = "http://localhost:8000"

# Example 1: List Songs (GET request)
response = requests.get(f"{BASE_URL}/list_songs?limit=5")
if response.status_code == 200:
    print("List of Songs:")
    print(response.json())
else:
    print("Failed to list songs:", response.text)

# Example 2: Get Song Info (GET request)
song_index = 1  # Change this to any valid index
response = requests.get(f"{BASE_URL}/song_info/{song_index}")
if response.status_code == 200:
    print("\nSong Info:")
    print(response.json())
else:
    print("Failed to get song info:", response.text)

# Example 3: Get Recommendations (POST request)
recommend_data = {
    "index": 1,  # Index of the song to get recommendations for
    "n_recommendations": 5  # Number of recommended songs
}
response = requests.post(f"{BASE_URL}/recommend", json=recommend_data)
if response.status_code == 200:
    print("\nRecommendations:")
    for song in response.json():
        print(song)
else:
    print("Failed to get recommendations:", response.text)
