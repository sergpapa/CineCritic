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
    title = "american Pie"
    url_end = "&s=" + title
    search = requests.get("https://www.omdbapi.com/?i=tt3896198&apikey=8acb1c61" + url_end).json()
    response = (search["Search"])
    movies_sorted = sort_movies(response)
    movies = list(mongo.db.movies.find())

    return render_template("get_movies.html", movies=movies, movies_sorted=movies_sorted)    

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")), debug=True)

