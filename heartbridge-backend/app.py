from flask import Flask, jsonify, request
import yaml
import os
import openai
from flask_cors import CORS

from pairwise_model_selector import select_pairwise_model
from dynamic_recommendation import generate_recommendation

# إعداد Flask
app = Flask(__name__)
CORS(app)

# مفتاح OpenAI من البيئة
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Heartbridge backend is running successfully."})

@app.route('/dynamic-recommendation', methods=['POST'])
def handle_dynamic_recommendation():
    try:
        data = request.json
        text = data.get("text", "")
        cluster = data.get("cluster", "The Silent Doubter")
        quiz_answers = data.get("quizAnswers", {})

        if not text:
            return jsonify({"error": "No dialogue text provided"}), 400

        selected_model = select_pairwise_model(cluster)

        payload = {
            "text": text,
            "cluster": cluster,
            "quiz_answers": quiz_answers,
            "model": selected_model
        }

        output = generate_recommendation(payload)
        return jsonify(output)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/ai-analyze', methods=['POST'])
def ai_analyze():
    try:
        data = request.json
        prompt = data.get("prompt", "")
        if not prompt:
            return jsonify({"error": "Missing prompt"}), 400

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "أنت مساعد نفسي خبير في العلاقات، تحلل المشاعر وتقدم توصيات واقعية."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        result = response.choices[0].message.content
        return jsonify({"response": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
