from fastapi import FastAPI, Request
import pickle
from pydantic import BaseModel
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

with open("recommender_data.pkl", "rb") as f:
    data = pickle.load(f)
    csr_data = data["csr_data"]
    movie_names = data["movie_names"]
    movie_to_row = data["movie_to_row"]
    model = data["model"]


def recommend_movies(movie_name, csr_data, movie_names, movie_to_row, model, n_recommendations=5):
    movie_idx = movie_to_row[movie_name]
    movie_vector = csr_data[movie_idx]

    distances, indices = model.kneighbors(movie_vector, n_neighbors=n_recommendations + 1)

    recommendations = []

    for rec_idx, rec_distance in zip(indices.flatten()[1:], distances.flatten()[1:]):
        recommendations.append((movie_names[rec_idx], rec_distance))

    return recommendations


class Features(BaseModel):
    name: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/recommend")
async def recommend(features: Features):
    name = features.name
    recommendations = recommend_movies(name, csr_data, movie_names, movie_to_row, model, n_recommendations=5)
    return {"recommendations": recommendations}


@app.get("/search-movies")
async def search_movies(query: str):
    """
    Return movie titles that contain the given query
    anywhere in the title (beginning, middle, or end).
    """
    q = query.strip().lower()
    if not q:
        return {"matches": []}

    # Safely convert movie_names depending on whether it is a list,
    # array, or another iterable structure.
    try:
        names_iterable = list(movie_names)
    except TypeError:
        names_iterable = movie_names

    matches = []
    for name in names_iterable:
        title = str(name)
        if q in title.lower():
            matches.append(title)
        if len(matches) >= 15:
            break

    return {"matches": matches}