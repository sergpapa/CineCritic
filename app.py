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

def top_rated(reviews, imdbID):
    most_likes = 0
    top_rated = None
    for review in reviews:
        if review["imdbID"] == imdbID:
            if review["NoStars"] > most_likes:
                most_likes =  review["NoStars"]  
                top_rated = review["review"]
    return top_rated


# Template rendering
@app.route("/")
@app.route("/movies_list")
def movies_list():
    movies = list(mongo.db.movies.find().sort({"_id": -1}))
    return render_template("movies_list.html", movies=movies)


@app.route("/search", methods=["GET", "POST"])
def search():
    movies = list(mongo.db.movies.find())
    title = request.form.get("searchMovies")
    url_end = "&s=" + str(title).replace(" ", "_")
    try:
        title = request.form.get("searchMovies")
        url_end = "&s=" + str(title).lower().replace(" ", "_")
        response = requests.get("https://www.omdbapi.com/?i=tt3896198&apikey=8acb1c61" + url_end)
        if response.status_code == 200:
            search = response.json()
            if "Search" in search:
                response = (search["Search"])
                movies_sorted = sort_movies(response)
                return render_template("search.html", movies_sorted=movies_sorted, movies=movies, title=title)
            else:
                flash("No such movie")
                return redirect(url_for("search"))
        else:
            flash(f"Error: {response.status_code} - {response.reason}")
    except requests.RequestException as e:
        flash(f"Error fulfilling request: {e}")
        return redirect(url_for("search"))
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
    movies = list(mongo.db.movies.find())
    existing_movie = mongo.db.movies.find_one({"imdbID": imdbID})
    if session["user"]:
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
                "added_by": session["user"],
                "reviews": 0
            }
            mongo.db.movies.insert_one(movie_to_add)
            movies = list(mongo.db.movies.find().sort({"_id": -1}))
            flash("Movie added successfully")
            return render_template("movies_list.html", movies=movies)
    else:
        flash("~ You must be logged in to add a movie ~")
    movies = list(mongo.db.movies.find())
    return redirect(url_for("search"))


@app.route("/movie/<imdbID>")
def movie(imdbID):
    movie = mongo.db.movies.find_one({"imdbID": imdbID})
    reviews = list(mongo.db.reviews.find())
    top = top_rated(reviews,imdbID)
    return render_template("movie.html", movie=movie, reviews=reviews, top=top)

@app.route("/add_review/<imdbID>", methods=["GET", "POST"])
def add_review(imdbID):
    movie = mongo.db.movies.find_one({"imdbID": imdbID})
    if request.method == "POST":
        review = {
            "review": request.form.get("add_review"),
            "movie": movie["title"],
            "imdbID": movie["imdbID"],
            "added_by": session["user"],
            "NoStars": 0,
            "liked_by": []
        }
        mongo.db.reviews.insert_one(review)
        mongo.db.movies.update_one({"imdbID": imdbID}, {"$inc":  {"reviews": 1}})
        flash("Review added successfully!")
        return redirect(url_for("movie", imdbID=movie["imdbID"]))
        
    return render_template("add_review.html", movie=movie)

@app.route("/edit_review/<review_id>/<imdbID>", methods=["GET", "POST"])
def edit_review(review_id, imdbID):
    movie = mongo.db.movies.find_one({"imdbID": imdbID})
    review_to_edit = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    if request.method == "POST":
        review = {
            "review": request.form.get("edit_review"),
        }
        mongo.db.reviews.update_one({"_id": ObjectId(review_id)}, {"$set": review})
        flash("Review edited successfully!")
        return redirect(url_for("movie", imdbID=movie["imdbID"]))
        
    return render_template("edit_review.html", movie=movie, review_to_edit=review_to_edit)

@app.route("/delete_review/<review_id>/<imdbID>")
def delete_review(imdbID, review_id):
    mongo.db.reviews.delete_one({"_id": ObjectId(review_id)})
    mongo.db.movies.update_one({"imdbID": imdbID}, {"$inc":  {"reviews": -1}})
    flash("Review successfully deleted")
    return redirect(url_for("movie", imdbID=imdbID))

@app.route("/rate_review/<review_id>/<imdbID>")
def rate_review(imdbID, review_id):
    movie = mongo.db.movies.find_one({"imdbID": imdbID})
    review_to_edit = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})

    star = {
        "NoStars": 1
    }

    like = {
        "liked_by": session["user"]
    }

    if session["user"] not in review_to_edit["liked_by"]:
        mongo.db.reviews.update_one({"_id": ObjectId(review_id)}, {"$inc":  star})
        mongo.db.reviews.update_one({"_id": ObjectId(review_id)}, {"$push":  like})
        return redirect(url_for("movie", imdbID=imdbID, review_to_edit=review_to_edit, movie=movie))
    else:
        flash("You already liked this review")
        return redirect(url_for("movie", imdbID=imdbID, review_to_edit=review_to_edit, movie=movie))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")), debug=True)

