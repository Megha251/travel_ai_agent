import json


def search_flights(source, destination):

    with open("data/flights.json", "r", encoding="utf-8") as file:
        flights = json.load(file)

    matching_flights = []

    # Exact match
    for flight in flights:

        flight_from = flight["from"].strip().lower()
        flight_to = flight["to"].strip().lower()

        if (
            flight_from == source.strip().lower()
            and flight_to == destination.strip().lower()
        ):

            matching_flights.append(flight)

    # If exact route exists
    if matching_flights:

        cheapest_flight = min(
            matching_flights,
            key=lambda x: x["price"]
        )

        return cheapest_flight

    # ===============================
    # FALLBACK ROUTE
    # ===============================

    # If no route found, suggest cheapest flight
    fallback_flight = min(
        flights,
        key=lambda x: x["price"]
    )

    fallback_flight["note"] = (
        f"No direct route found from {source} to {destination}. "
        f"Showing cheapest available route instead."
    )

    return fallback_flight
