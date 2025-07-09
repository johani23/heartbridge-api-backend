def select_pairwise_model(cluster):
    models = {
        "The Silent Doubter": "model_silent",
        "The Idealist": "model_ideal",
        "The Burnt Survivor": "model_burnt",
        "The Data-Lover": "model_data"
    }
    return models.get(cluster, "model_default")
# Contents of pairwise_model_selector.py
