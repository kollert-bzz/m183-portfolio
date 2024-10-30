from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>M183 Portfolio | Timo Koller</h1>'


@app.route('/example', methods=['GET'])
def example():
    return jsonify({'example': 'Dies ist ein Beispiel-Endpunkt!'})


if __name__ == '__main__':
    app.run(debug=True)
