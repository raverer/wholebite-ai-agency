def get_audience_from_keyword(keyword):

    keyword = keyword.lower()

    if "protein" in keyword:
        return "People looking to increase protein intake through simple everyday meals"

    elif "cholesterol" in keyword:
        return "People looking to improve cholesterol levels through better food choices"

    elif "ldl" in keyword:
        return "People looking to improve cholesterol levels through better food choices"

    elif "fat loss" in keyword:
        return "People trying to lose weight without extreme diets"

    elif "weight loss" in keyword:
        return "People trying to lose weight without extreme diets"

    elif "meal prep" in keyword:
        return "Busy professionals trying to eat healthy consistently"

    elif "gut health" in keyword:
        return "Adults over 30 focused on improving long-term health"

    else:
        return "Indians seeking practical healthy eating solutions using familiar foods"