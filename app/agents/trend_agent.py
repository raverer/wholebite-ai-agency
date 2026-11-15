from pytrends.request import TrendReq
import random


TREND_CATEGORIES = {
    "protein": [
        "high protein breakfast",
        "protein coffee",
        "protein snacks"
    ],
    "gut_health": [
        "gut health foods",
        "fermented foods"
    ],
    "cholesterol": [
        "cholesterol lowering foods"
    ],
    "meal_prep": [
        "meal prep ideas"
    ]
}


def get_trending_keyword():

    all_keywords = []

    for values in TREND_CATEGORIES.values():
        all_keywords.extend(values)

    keyword = random.choice(all_keywords)

    try:

        pytrends = TrendReq(
            hl="en-US",
            tz=330
        )

        pytrends.build_payload([keyword])

        related = pytrends.related_queries()

        top_queries = related[keyword]["top"]

        if top_queries is not None:

            filtered = []

            for query in top_queries["query"]:

                query = query.lower()

                banned_words = [
                    "book",
                    "movie",
                    "netflix",
                    "amazon",
                    "episode",
                    "series"
                ]

                if not any(
                    word in query
                    for word in banned_words
                ):
                    filtered.append(query)

            if filtered:
                keyword = filtered[0]

    except Exception:
        pass

    return keyword