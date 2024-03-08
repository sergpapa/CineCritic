import os 
import requests
from flask import (Flask, flash,
                    render_template, redirect,
                    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# functionality functions

def sort_movies(movie_list):
    movies_sorted = []
    for movie in movie_list:
        if movie["Type"] == "movie":
            movies_sorted.append(movie)
    return movies_sorted        


# Template rendering

@app.route("/")
@app.route("/get_movies")
def get_movies():
    movies = list(mongo.db.movies.find())
    return render_template("get_movies.html", movies=movies)

@app.route("/search", methods=["GET", "POST"])
def search():
    title = request.form.get("searchMovies")
    url_end = "&s=" + str(title).replace(" ", "_")
    search = requests.get("https://www.omdbapi.com/?i=tt3896198&apikey=8acb1c61" + url_end).json()
    response = (search["Search"])
    movies_sorted = sort_movies(response)
    return render_template("get_movies.html", movies_sorted=movies_sorted)

@app.route("/add_movie/<imdbID>")
def add_movie(imdbID):
    existing_movie = mongo.db.movies.find_one({"imdbID": imdbID})
    if existing_movie:
        flash("Movie already in database")
    else:
        movie = requests.get("https://www.omdbapi.com/?i=" + imdbID + "&apikey=8acb1c61").json()
        print("movie= ", movie)
        print(type(movie))
        movie_to_add = {
            "title": movie["Title"],
            "year": movie["Year"],
            "poster": movie["Poster"],
            "imdbID": movie["imdbID"]
        }
        mongo.db.movies.insert_one(movie_to_add)
        flash("Movie added successfully")
    return render_template("get_movies.html")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")), debug=True)

