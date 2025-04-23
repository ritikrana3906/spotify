import os

folders = [
    "spotify-recommender/data",
    "spotify-recommender/models",
    "spotify-recommender/notebooks",
    "spotify-recommender/src",
    "spotify-recommender/src/recommender",
]

files = [
    "spotify-recommender/README.md",
    "spotify-recommender/requirements.txt",
    "spotify-recommender/.gitignore",
    "spotify-recommender/src/recommender/__init__.py",
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in files:
    with open(file, "w") as f:
        pass

print("✅ Project folder structure created!")