def calculate_stats(list_analyzer: list[str]) -> tuple | None:
    result_dict = {
        "negative": 0,
        "positive": 0,
        "neutral": 0,
    }

    for item in list_analyzer:
        label = item["sentiment"]
        result_dict[label] += 1

    total = sum(result_dict.values())

    if total == 0:
        return None

    final_stats = {}

    for label, count in result_dict.items():
        final_stats[label+"_percent"] = round((count / total) * 100, 2)

    return result_dict, final_stats
