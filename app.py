from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/recommendation', methods=['POST'])
def get_recommendation():
    data = request.json
    questionnaire = data.get('questionnaire', {})
    conversation = data.get('conversation', "")

    # Simple logic for clustering (dummy)
    cluster = "Idealist" if questionnaire.get('mom_education', '') == 'University' else "Realist"

    # Dummy recommendation logic
    if "love" in conversation.lower():
        recommendation = "العلاقة واعدة لكنها تحتاج وضوح عاطفي."
    else:
        recommendation = "ينقص العلاقة بعد وجداني واضح، ننصح بمصارحة صادقة."

    return jsonify({
        "cluster": cluster,
        "recommendation": recommendation
    })

if __name__ == '__main__':
    app.run(debug=True)