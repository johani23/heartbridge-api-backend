def select_pairwise_model(cluster_name):
    return {
        "The Idealist": "hope_vs_blindness",
        "The Silent Doubter": "guarded_vs_genuine",
        "The Burnt Survivor": "trauma_vs_trust",
        "The Rescuer": "giver_vs_empty",
        "The Echoed": "repeat_vs_renewal"
    }.get(cluster_name, "default_model")