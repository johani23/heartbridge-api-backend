from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/ai-analyze', methods=['POST'])
@app.route('/analyze', methods=['POST'])  # alias to match frontend route
def ai_analyze():
    try:
        data = request.json
        prompt = data.get("prompt", "")
        if not prompt:
            return jsonify({"error": "Missing prompt"}), 400

        print(f"[DEBUG] Received prompt: {prompt}")

        response = client.chat.completions.create(
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
        import traceback
        print("[ERROR in /ai-analyze]")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500
