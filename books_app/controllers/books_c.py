from flask import redirect, render_template, request
from books_app import app
from books_app.models.books_m import Book

@app.route('/books', methods=["GET", "POST"])
def handleBooks():
    if request.method == "GET":
        booksList = Book.getBooks()
        return render_template("books.html", books=booksList)