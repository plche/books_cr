from books_app.config.mysqlconnection import connectToMySQL

class Author:
    def __init__(self, id, name, created_at, updated_at):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def getAuthors(cls):
        query = "SELECT * FROM authors;"
        queryResult = connectToMySQL("books_schema").query_db(query)
        authorsList = []
        for author in queryResult:
            authorsList.append(Author(author["id"], author["name"], author["created_at"], author["updated_at"]))
        return authorsList

    @classmethod
    def addAuthor(cls, newAuthor):
        query = "INSERT INTO authors(name) VALUES(%(name)s);"
        queryResult = connectToMySQL("books_schema").query_db(query, newAuthor)
        return queryResult