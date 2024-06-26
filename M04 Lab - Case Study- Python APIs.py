from flask import Flask, request, jsonify

app = Flask(__name__)
books = {}
 

@app.route('/books', methods=['POST'])
def create_book():
    global current_id
    data = request.get_json()
    books[current_id] = {**data, 'id': current_id}
    return jsonify(books[current_id - 1])

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(list(books.values()))

@app.route('/books/<int:book_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_book(book_id):
    if request.method == 'GET':
        return jsonify(books.get(book_id, 'Book not found'))
    elif request.method == 'PUT':
        if book_id in books:
            data = request.get_json()
            books[book_id].update(data)
            return jsonify(books[book_id])
        else:
            return 'Book not found', 404
    elif request.method == 'DELETE':
        if book_id in books:
            del books[book_id]
            return f'Book with id {book_id} deleted successfully', 200
        else:
            return 'Book not found', 404

if __name__ == '__main__':
    app.run(debug=True)
