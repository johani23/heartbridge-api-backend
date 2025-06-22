
def detect_cluster(text):
    if 'دخل' in text or 'خوف' in text:
        return 'القلق/الانسحاب'
    elif 'حب' in text or 'اهتمام' in text:
        return 'الارتباط العاطفي'
    elif 'ملل' in text or 'طفش' in text:
        return 'البرود/الانسحاب'
    else:
        return 'نمط غير محدد'
