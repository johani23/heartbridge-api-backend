def generate_recommendation(cluster_name, axis_flags):
    if cluster_name == "The Rescuer" and axis_flags.get("emotional_gap") and axis_flags.get("financial_imbalance"):
        return {
            "title": "العلاقة مشروطة.",
            "body": "يظهر أنك تميل للعطاء العاطفي والمادي بلا حدود، لكن الطرف الآخر لا يُظهر نفس المستوى من الالتزام. ننصح بإعادة تقييم التوازن في العلاقة، لأن استمرارك بهذا النسق قد يؤدي إلى استنزاف لا تلاحظه إلا متأخرًا."
        }

    if cluster_name == "The Silent Doubter" and axis_flags.get("emotional_silence"):
        return {
            "title": "العلاقة واعدة لكن تحتاج انفتاحًا.",
            "body": "يميل نمطك إلى اختبار العلاقة بصمت. ننصح بحوار صريح وواضح لتحديد ما إذا كان الحذر نابعًا من حدسك أم من خوف قديم."
        }

    return {
        "title": "العلاقة تحتاج حوارًا أعمق.",
        "body": "نوصي بمواجهة الأسئلة الصعبة بصراحة، فبعض الغموض الآن قد يتحول لاحقًا إلى استياء يصعب التراجع عنه."
    }