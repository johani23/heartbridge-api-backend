
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
    cluster_input = data.get("cluster", None)  # نأخذ الكلستر إذا أرسله الواجهة

    # إذا فيه كلستر جاهز من الاستبيان نستخدمه
    if cluster_input:
        cluster = cluster_input
        response_text = "🧠 تم دمج نتيجة الاستبيان مع تحليل الرسالة بنجاح."
    else:
        # تحليل بدائي بناءً على الكلمات
        if "أخاف" in message or "من طرف واحد" in message:
            cluster = "قلق التعلق"
            response_text = "🚨 يظهر قلق من جانب واحد في العلاقة. قد تكون بحاجة إلى طمأنة أو وضوح من الطرف الآخر."
        elif "احتاج" in message or "اهتمام" in message:
            cluster = "شغف عاطفي"
            response_text = "💬 توجد مؤشرات على تعلق عاطفي قوي أو احتياج مستمر للتقدير."
        else:
            cluster = "حيادية ضعيفة"
            response_text = "🌿 لا توجد مؤشرات قوية لخلل واضح في النص المُرسل."

    return jsonify({
        "input": message,
        "cluster": cluster,
        "analysis": response_text
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
