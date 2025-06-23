from flask import Flask, request, jsonify, session
from flask_cors import CORS
from utils.pairwise_model_selector import select_pairwise_model
from recommendation_engine.dynamic_recommendation import generate_recommendation
import yaml
import os

app = Flask(__name__)
CORS(app)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "default_secret")

# ØªØ­Ù…ÙŠÙ„ Ø£Ø³Ø¦Ù„Ø© popup
with open("assets/prompts/popup_prompts.yaml", "r", encoding="utf-8") as f:
    popup_prompts = yaml.safe_load(f)

@app.route("/get-popup", methods=["GET"])
def get_popup():
    cluster = session.get("cluster_name", "The Idealist")
    prompts = popup_prompts.get(cluster, [])
    return jsonify({"cluster": cluster, "prompt": prompts[0] if prompts else "Ù„Ø§ ÙŠÙˆØ¬Ø¯ Ø³Ø¤Ø§Ù„ Ø­Ø§Ù„ÙŠØ§Ù‹"})

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    cluster = session.get("cluster_name", "The Idealist")
    flags = data.get("axis_flags", {})
    recommendation = generate_recommendation(cluster, flags)
    return jsonify(recommendation)

@app.route("/")
def index():
    return "Heartbridge backend is running."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)
