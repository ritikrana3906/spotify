# 🎧 Spotify-Style Music Recommendation System

A full-fledged backend project that replicates Spotify's recommendation system using collaborative filtering, content-based filtering, and hybrid models. Includes API endpoints, model training, user simulation, and containerization using Docker.

---

## 📌 Project Goals

- Build a scalable recommendation backend from scratch
- Simulate real-world music and user behavior
- Use machine learning models to recommend songs
- Serve recommendations through a FastAPI backend
- Containerize the full system with Docker and optionally deploy with Kubernetes

---

## 🧱 Project Structure (Modular Systems)

### 🔹 SYSTEM 1: Data Pipeline & Ingestion
- Integrate with Spotify Web API using `spotipy`
- Fetch song metadata, audio features, and playlist data
- Store data in local files or PostgreSQL database
- Ingestion script: `data_ingestor.py`

### 🔹 SYSTEM 2: Recommender Engine
- **Content-Based Filtering** using audio features and cosine similarity
- **Collaborative Filtering** with matrix factorization (`implicit` or `surprise`)
- Optional: Hybrid recommender combining both
- Train and save models (`joblib`/`pickle`)

### 🔹 SYSTEM 3: API Layer
- Backend built using **FastAPI**
- Endpoints:
  - `GET /recommend/song/{track_id}`
  - `POST /recommend/user/`
- Connects to models and optionally the database
- Includes unit testing for endpoints

### 🔹 SYSTEM 4: User & Playlist Simulation
- Generate mock users and simulate playlists
- Build a user-song matrix for collaborative filtering

### 🔹 SYSTEM 5: Database Layer (Optional)
- Use PostgreSQL to store:
  - Songs
  - Users
  - Playlists
- Connect API layer to query data dynamically

### 🔹 SYSTEM 6: Frontend Interface (Optional)
- Use **Streamlit** or **Gradio** for visualizing recommendations
- Search for a song and see top recommendations
- Interactive filters by genre, mood, etc.

### 🔹 SYSTEM 7: Containerization & Deployment
- Dockerize all services (API, model, DB)
- Use `docker-compose` for multi-container orchestration
- Optionally set up Kubernetes (minikube) for simulation
- Deploy-ready for cloud (e.g., GCP, AWS, Heroku)

---

## 🧰 Tech Stack

- **Languages**: Python
- **ML Libraries**: Scikit-learn, Surprise, Implicit, FAISS
- **API**: FastAPI
- **Database**: PostgreSQL (or MongoDB)
- **Frontend**: Streamlit (optional)
- **DevOps**: Docker, Docker Compose, Kubernetes (optional)
- **Spotify API**: Spotipy

---

## 🚀 Project Timeline

| Week | Tasks                                         |
|------|-----------------------------------------------|
| 1    | Data ingestion + Content-based recommender    |
| 2    | Collaborative filtering + FastAPI backend     |
| 3    | Dockerization + Frontend + Final polish       |

---

## 📂 Folder Structure
