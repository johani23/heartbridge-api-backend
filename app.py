
from flask import Flask, request, jsonify
from flask_cors import CORS
from detectCluster import detect_cluster  # تأكد أن هذه الدالة موجودة ومستوردة

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get("text", "")
    result = detect_cluster(text)
    return jsonify({"cluster": result})

if __name__ == '__main__':
    app.run(debug=True)
