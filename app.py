
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # تمكين الاتصال من الواجهة الأمامية

@app.route("/")
def home():
    return "✅ Heartbridge API is live and working!"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    message = data.get("message", "").lower()

    cluster = "غير مصنف"
    analysis = "يرجى كتابة حوار واضح لتحليله بدقة."
    risk_level = "منخفض"
    recommendation = "شارك موقفًا أو مشاعرك بوضوح أكثر."

    if "أخاف" in message or "من طرف واحد" in message:
        cluster = "قلق التعلق"
        analysis = "🚨 يظهر قلق من جانب واحد في العلاقة. قد تكون بحاجة إلى طمأنة أو وضوح من الطرف الآخر."
        risk_level = "مرتفع"
        recommendation = "ناقش مشاعرك بصدق وتأكد من توازن العلاقة."

    elif "أحتاج" in message or "احتاجه" in message or "أفتقد" in message:
        cluster = "تعلق عاطفي"
        analysis = "🧲 توجد مؤشرات على تعلق عاطفي قوي، قد يكون بسبب الاحتياج المستمر أو البحث عن الأمان."
        risk_level = "متوسط"
        recommendation = "قيّم مصدر الاحتياج وهل هو صحي أو تعويضي."

    elif "أمي" in message or "امي" in message:
        cluster = "أثر الأم"
        analysis = "🧬 يظهر أثر قوي لعلاقتك مع الأم في طريقة تعاملك العاطفي الحالي."
        risk_level = "متوسط"
        recommendation = "استكشاف العلاقة مع الأم قد يساعد في فهم مشاعرك وتوقعاتك."

    elif "ثقافتنا" in message or "بيئتنا" in message or "عاداتنا" in message:
        cluster = "الضغط الثقافي"
        analysis = "📚 يبدو أن هناك ضغطًا ناتجًا من البيئة أو الثقافة يؤثر على رؤيتك للعلاقة."
        risk_level = "منخفض"
        recommendation = "فرّق بين صوتك الداخلي وتوقعات المجتمع."

    return jsonify({
        "input": message,
        "cluster": cluster,
        "analysis": analysis,
        "risk_level": risk_level,
        "recommendation": recommendation
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
