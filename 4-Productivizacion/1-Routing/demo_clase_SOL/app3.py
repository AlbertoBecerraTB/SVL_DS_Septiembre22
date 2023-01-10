from flask import Flask, request
import sqlite3

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/v1/resources/books/all', methods=['GET'])
def get_all():
    connection = sqlite3.connect('demo_clase/books.db')
    cursor = connection.cursor()

    select_books = "SELECT * FROM books"

    result = cursor.execute(select_books).fetchall()

    connection.close()

    return {'books': result}


@app.route('/api/v1/resources/book/<string:author>', methods=['GET'])
def get_by_author(author):
    connection = sqlite3.connect('demo_clase/books.db')
    cursor = connection.cursor()

    select_books = "SELECT * FROM books WHERE author=?"

    result = cursor.execute(select_books, (author,)).fetchall()

    connection.close()

    return {'books': result}



@app.route('/api/v1/resources/book/filter', methods=['GET'])
def filter_table():
    query_parameters = request.get_json()

    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')

    connection = sqlite3.connect('demo_clase/books.db')
    cursor = connection.cursor()

    query = "SELECT * FROM books WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if published:
        query += ' published=? AND'
        to_filter.append(published)
    if author:
        query += ' author=? AND'
        to_filter.append(author)
    if not (id or published or author):
        return "page not found 404"


    query = query[:-4] + ';'

    result = cursor.execute(query, to_filter).fetchall()

    connection.close()


    return {'books': result}



app.run()
