def generate_itinerary(places):

    itinerary = []

    for i, place in enumerate(places):

        itinerary.append(
            f"Day {i+1}: Visit {place['name']}"
        )

    return itinerary