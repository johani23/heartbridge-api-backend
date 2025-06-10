
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    return jsonify({
        "message": "تحليل مبدئي للمحادثة",
        "input": data
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
