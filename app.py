
# src/app.py

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
    # هذا مثال توضيحي لتحليل مبسط، غيّره حسب منطقك التحليلي
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    text = data.get("text", "")
    result = {
        "original": text,
        "length": len(text),
        "is_long": len(text) > 100
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
