import pickle
import joblib
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
import logging

class SongRecommender:
    def __init__(self):
        self.model_data = joblib.load("app/model/data_new.pkl")
        self.scaler = self.model_data['scaler']
        self.knn = self.model_data['knn']
        self.df = self.model_data['data']
        self.feature_cols = self.model_data['features']

        
    def recommend(self, index, n_recommendations=5):
        # Get song's feature vector for the index
        song_features = self.df.iloc[index][self.feature_cols].values.reshape(1, -1)
        song_scaled = self.scaler.transform(song_features)
        
        # Find nearest neighbors
        distances, indices = self.knn.kneighbors(song_scaled, n_neighbors=n_recommendations)
        
        # Fetch recommended song details
        recommended_songs = self.df.iloc[indices[0]]
        
        print(f"LENGTH OF RECOMMENDED SONGS: {recommended_songs.shape[0]}")
        # Return a list of recommended song titles and their similarity
        # recommendations = [
        #     {"track_name": row['track_name'], "artist_name": row['artist_name'], "distance": distances[0][i]}
        #     for i, row in recommended_songs.iterrows()
        # ]
        recommendations = [
                {
                    "track_name": row['track_name'],
                    "artist_name": row['artist_name'],
                    "distance": distances[0][idx]
                }
            for idx, (_, row) in enumerate(recommended_songs.iterrows())
            ]
        
        return recommendations

    def list_songs(self, limit=10):
        return self.df.head(limit)[['track_name', 'artist_name']].to_dict(orient='records')
    
    def get_song_info(self, index):
        try:
            song = self.df.iloc[index]
            return {
                "track_name": song['track_name'],
                "artist_name": song['artist_name'],
                # "year": song['year'],
                "danceability": song['danceability'],
                "energy": song['energy'],
                "tempo": song['tempo'],
                "valence": song['valence']
            }
        except IndexError:
            return None