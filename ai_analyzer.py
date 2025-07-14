@app.route('/ai-analyze', methods=['POST'])
@app.route('/analyze', methods=['POST'])  # alias to match frontend route
def ai_analyze():
    try:
        data = request.json
        prompt = data.get("prompt", "")
        if not prompt:
            return jsonify({"error": "Missing prompt"}), 400

        print(f"[DEBUG] Received prompt: {prompt}")

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "أنت مساعد نفسي خبير في العلاقات، تحلل المشاعر وتقدم توصيات واقعية."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        result = response.choices[0].message.content
        return jsonify({"response": result})

    except Exception as e:
        import traceback
        print("[ERROR in /ai-analyze]")
        traceback.print_exc()  # يطبع الخطأ كاملًا في اللوق داخل Render
        return jsonify({"error": str(e)}), 500
