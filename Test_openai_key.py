import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    models = client.models.list()
    print("✅ المفتاح يعمل. النماذج:")
    for m in models.data:
        print(f"- {m.id}")
except Exception as e:
    print("❌ المفتاح غير صالح أو في مشكلة:")
    print(e)
