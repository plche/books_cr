from flask import flash, redirect, render_template, request
from books_app import app
from books_app.models.authors_m import Author

@app.route('/', methods=["GET"])
def home():
    return redirect('/authors')

@app.route('/authors', methods=["GET", "POST"])
def handleAuthors():
    if request.method == "GET":
        authorsList = Author.getAuthors()
        return render_template("authors.html", authors=authorsList)

@app.route('/authors/add', methods=["POST"])
def addAuthorsNew():
    newAuthor = {
        "name" : request.form["name"],
    }
    result = Author.addAuthor(newAuthor)
    if type(result) is not int:
        flash("There was a problem registering the new author, please try again", "addauthornew")
    return redirect('/authors')