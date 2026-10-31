from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "UP",
        "service": "ms-python",
        "language": "Python 3.11"
    }), 200

@app.route('/api/v1/calc/add/<int:a>/<int:b>', methods=['GET'])
def add(a, b):
    result = a + b
    return jsonify({
        "operation": "addition",
        "a": a,
        "b": b,
        "result": result
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)