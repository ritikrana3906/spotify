import pandas as pd
import os
import json
from dotenv import load_dotenv

load_dotenv("spotify-recommender/notebooks/details.env")

data_path = os.getenv("DATA_PATH")
ls = os.listdir(data_path)
print(ls[0])

with open(os.path.join(data_path, ls[0]), "r") as f:
    data = json.load(f)

print(data.keys())
# print(data['playlists'][0].keys())
# data2 = data['playlists'][0]['tracks']

# df = pd.DataFrame(data2)
# print(df.head())
# df.to_csv("spotify-recommender/notebooks/first_json_as_dataset.csv", index=False)

df_ls = []
for data in data["playlists"]:
    name = data["name"]
    collaborative = data["collaborative"]
    pid = data["pid"]
    modified_at = data["modified_at"]
    num_tracks = data["num_tracks"]
    num_albums = data["num_albums"]
    num_followers = data["num_followers"]
    for tracks in data["tracks"]:
        pos = tracks["pos"]
        artist_name = tracks["artist_name"]
        track_uri = tracks["track_uri"]
        track_name = tracks["track_name"]
        album_uri = tracks["album_uri"]
        duration_ms = tracks["duration_ms"]
        album_name = tracks["album_name"]

        df_ls.append(
            {
                "name": name,
                "collaborative": collaborative,
                "pid": pid,
                "modified_at": modified_at,
                "num_tracks": num_tracks,
                "num_albums": num_albums,
                "num_followers": num_followers,
                "pos": pos,
                "artist_name": artist_name,
                "track_uri": track_uri,
                "track_name": track_name,
                "album_uri": album_uri,
                "duration_ms": duration_ms,
                "album_name": album_name,
            }
        )

df = pd.DataFrame(df_ls)
# print(df.shape)
# df.to_csv("spotify-recommender/notebooks/flattened_json_first.csv", index=False)
# print(df['name'].value_counts())
# print(df.columns)

# print(df[df['name'] == 'Country'].shape)