import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_recommendation(payload):
    text = payload.get("text", "")
    cluster = payload.get("cluster", "The Silent Doubter")
    answers = payload.get("quiz_answers", {})
    model = payload.get("model", "default")

    prompt = f"""
    تحليل لحالة عاطفية ضمن نمط: {cluster}.
    نص الحوار:\n{text}
    بيانات المستخدم:\n{answers}
    استخدم النموذج: {model}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "أنت مساعد عاطفي ذكي تحلل الحوارات وتقدم توصيات نفسية ناضجة."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return {"output": response.choices[0].message.content, "popups": []}
# Contents of dynamic_recommendation.py
