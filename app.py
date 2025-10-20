from flask import Flask, jsonify, request

# Create a Flask application
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to my Flask App!"

# Example API route (GET)
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")

# Example API route (POST)
@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    num1 = data.get('num1', 0)
    num2 = data.get('num2', 0)
    result = num1 + num2
    return jsonify(result=result)

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
