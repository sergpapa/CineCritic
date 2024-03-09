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

@app.route("/movies_list")
def movies_list():
    movies = list(mongo.db.movies.find())
    return render_template("movies_list.html", movies=movies)

@app.route("/")
@app.route("/search", methods=["GET", "POST"])
def search():
    movies = list(mongo.db.movies.find())
    title = request.form.get("searchMovies")
    url_end = "&s=" + str(title).replace(" ", "_")
    search = requests.get("https://www.omdbapi.com/?i=tt3896198&apikey=8acb1c61" + url_end).json()
    response = (search["Search"])
    movies_sorted = sort_movies(response)
    return render_template("search.html", movies_sorted=movies_sorted, movies=movies, title=title)

## Prifile functionality from Taskmanager Project
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            flash("User already exists")
            return redirect(url_for("register"))

        register =  {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration successfull")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                flash("Username and/or password is incorrect")
                return redirect(url_for("login"))
        else:
            flash("Username and/or password is incorrect")
            return redirect(url_for("login"))  
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("profile.html", username=username)

    return render_template("login.html")

@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

## end of profile funcitonality

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
            "imdbID": movie["imdbID"],
            "added_by": session["user"]
        }
        mongo.db.movies.insert_one(movie_to_add)
        flash("Movie added successfully")
    movies = list(mongo.db.movies.find())
    return render_template("movies_list.html", movies=movies)


@app.route("/add_review/<imdbID>")
def add_review(imdbID):
    movie = mongo.db.movies.find_one({"imdbID": imdbID})
    return render_template("add_review.html", movie=movie)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")), debug=True)

