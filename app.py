from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({"message": "Heartbridge backend is running successfully."})

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    text = data.get("text", "")
    return jsonify({
        "original": text,
        "length": len(text),
        "is_long": len(text) > 100
    })