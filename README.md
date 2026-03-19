# MovieMatch

A simple movie recommendation web app built with **FastAPI** and a **KNN-based recommendation model**.

You can search for a movie title, choose one from the suggestions, and get **5 similar movie recommendations**.

## Features

- Live movie title search
- 5 similar movie recommendations
- Similarity score display
- FastAPI backend
- HTML/CSS/JavaScript frontend

## Project Structure

```text
movie-recommender/
│
├── app.py
├── templates/
│   └── index.html
├── movie_recommender_training.ipynb
├── requirements.txt
├── .gitignore
├── README.md
└── recommender_data.pkl
```

## Installation

Clone the repository and open the project folder:

```bash
git clone <your-repo-url>
cd movie-recommender
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Download the model file

The trained model file is not included in the repository because it is large.

Download **`recommender_data.pkl`** from Google Drive:

[Download recommender_data.pkl](https://drive.google.com/uc?export=download&id=1Fneg3MAFcoibTIhTCOLLrg1A0f81o34P)

After downloading it, place the file in the **project root folder**, in the **same location as `app.py`**.

Example:

```text
movie-recommender/
├── app.py
├── recommender_data.pkl
├── README.md
└── ...
```

## Dataset

The original dataset is also too large to keep in the repository.

You can download the raw **MovieLens 32M** dataset here:

[MovieLens 32M Dataset](https://grouplens.org/datasets/movielens/)

You only need the raw dataset if you want to **retrain the model** in the notebook.

If you only want to **run the app**, downloading **`recommender_data.pkl`** is enough.

## Run the app

Make sure:

- `recommender_data.pkl` is in the same folder as `app.py`
- your HTML file is inside `templates/index.html`

Then start the app with:

```bash
uvicorn app:app --reload
```

Open this in your browser:

```text
http://127.0.0.1:8000
```

## Notes

- `recommender_data.pkl` is intentionally kept outside the repo because of its size.
- The notebook is included for training and experimentation.
- The app uses the saved pickle file directly at startup.
