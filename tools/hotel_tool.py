import json


def recommend_hotels(city):

    with open("data/hotels.json", "r", encoding="utf-8") as file:

        hotels = json.load(file)

    matching_hotels = []

    for hotel in hotels:

        hotel_city = hotel["city"].strip().lower()

        if hotel_city == city.strip().lower():

            matching_hotels.append(hotel)

    if not matching_hotels:

        return "No hotels found"

    best_hotel = max(
        matching_hotels,
        key=lambda x: x["stars"]
    )

    return best_hotel