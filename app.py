from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # ← هذه السطر يحل مشكلة CORS

@app.route("/")
def home():
    return "✅ Heartbridge API is live and working!"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    message = data.get("message", "")
    return jsonify({
    "input": message,
    "analysis": "🧠 تحليل تجريبي: محتوى الرسالة تم استقباله بنجاح."
})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
