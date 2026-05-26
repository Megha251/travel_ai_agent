import json


def suggest_places(city):

    with open("data/places.json", "r", encoding="utf-8") as file:

        places = json.load(file)

    matching_places = []

    for place in places:

        place_city = place["city"].strip().lower()

        if place_city == city.strip().lower():

            matching_places.append(place)

    if not matching_places:

        return "No places found"

    top_places = sorted(
        matching_places,
        key=lambda x: x["rating"],
        reverse=True
    )

    return top_places[:5]