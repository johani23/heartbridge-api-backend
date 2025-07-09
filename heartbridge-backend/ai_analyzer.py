import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # أو "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "أنت مساعد نفسي خبير في العلاقات، تحلل المشاعر وتقدم توصيات عاطفية واقعية."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content
# Contents of ai_analyzer.py
