from flask import Flask, jsonify, request
import yaml

from pairwise_model_selector import select_model
from dynamic_recommendation import generate_recommendation  # إذا كنت تبي توصيات ذكية

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Heartbridge backend is running successfully."})

@app.route('/popup-prompts', methods=['GET'])
def get_popup_prompts():
    try:
        with open('popup_prompts.yaml', 'r', encoding='utf-8') as file:
            prompts = yaml.safe_load(file)
        return jsonify(prompts)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/select-model', methods=['POST'])
def handle_model_selection():
    try:
        data = request.json
        pattern_1 = data.get("pattern_1")
        pattern_2 = data.get("pattern_2")

        if not pattern_1 or not pattern_2:
            return jsonify({"error": "Missing required patterns"}), 400

        selected = select_model(pattern_1, pattern_2)
        return jsonify({"selected_model": selected})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/dynamic-recommendation', methods=['POST'])
def handle_dynamic_recommendation():
    try:
        data = request.json
        output = generate_recommendation(data)  # تأكد أن هذه الدالة موجودة
        return jsonify(output)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
