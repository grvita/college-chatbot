from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot_logic import find_response

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    response = find_response(message)
    return jsonify({'response': response})

@app.route('/')
def home():
    return "College Chatbot Backend Running!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
