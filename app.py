
from flask import Flask, request, jsonify
from detectCluster import detect_cluster

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.get_json()
    text = data.get('text', '')
    result = detect_cluster(text)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
