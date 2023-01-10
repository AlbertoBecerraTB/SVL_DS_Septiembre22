from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True

books = [ 
            {'id': 0, 
            'title': 'A Fire Upon the Deep', 
            'author': 'Vernor Vinge', 
            'first_sentence': 'The coldsleep itself was dreamless.', 
            'year_published': '1992'},
            
            {'id': 1, 
            'title': 'The Ones Who Walk Away From Omelas', 
            'author': 'Ursula K. Le Guin', 
            'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.', 
            'published': '1973'},

            {'id': 2, 
            'title': 'Dhalgren', 
            'author': 'Samuel R. Delany', 
            'first_sentence': 'to wound the autumnal city.', 
            'published': '1975'} 
        ]

# GET Display all the books
@app.route('/api/v1/resources/books/all', methods=['GET']) 
def api_all():
    return jsonify(books)

# GET ?id=x -> Display the book with specified id
# POST {id:, title:, author:, fist_sentence:, published:} -> Create this book
@app.route('/api/v1/resources/books', methods=['GET', 'POST']) 
def api_id():

    if request.method == 'GET':
        if 'id' in request.args: 
            id = int(request.args['id']) 
        else: 
            return "Error: No id field provided. Please specify an id." 
    
        results = [] 
        for book in books: 
            if book['id'] == id: 
                results.append(book) 
    
        return jsonify(results)

    if request.method == 'POST':
        data = request.get_json() 
        books.append(data) 
        return jsonify(data), 201

# GET /id -> Displays the books with the specified id
@app.route('/api/v1/resources/books/<int:id>', methods=['GET']) 
def api_id_2(id):
    results = [] 
    for book in books: 
        if book['id'] == id: 
            results.append(book) 
    return jsonify(results)

# GET /<title> -> Displays the books with the specified title name
@app.route('/api/v1/resources/books/<string:title>', methods=['GET'])
def api_title(title):
    results = []
    for book in books:
        if book['title'] == title:
            results.append(book)

    if results == []:
        return jsonify({'MessageError': 'Title Not Available'})

    return jsonify(results)

# GET {id:int} -> Displays the books with the specified id
@app.route('/api/v2/resources/books', methods=['GET']) 
def get_by_id(): 
    id = int(request.get_json()['id']) 
    for book in books: 
        if book['id'] == id: 
            return jsonify(book) 
    return jsonify({'message': "Book not found"})

app.run(port=5000)