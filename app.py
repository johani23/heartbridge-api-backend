from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "✅ Heartbridge API is live and working!"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    message = data.get("message", "")

    # تحليل بدائي مبني على الكلمات المفتاحية
    if "أخاف" in message or "من طرف واحد" in message:
        cluster = "قلق التعلق"
        response_text = "🚨 يظهر قلق من جانب واحد في العلاقة. قد تكون بحاجة إلى طمأنة أو وضوح من الطرف الآخر."
    elif "أشتاق" in message or "أحتاجه" in message:
        cluster = "احتياج عاطفي"
        response_text = "💡 توجد مؤشرات على تعلق عاطفي قوي أو شعور بالاحتياج المستمر."
    else:
        cluster = "غير مصنّف"
        response_text = "🌿 لا توجد مؤشرات قوية لخلل واضح في النص المُرسل."

    return jsonify({
        "input": message,
        "cluster": cluster,
        "analysis": response_text
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
