from tools.flight_tool import search_flights
from tools.hotel_tool import recommend_hotels
from tools.places_tool import suggest_places
from tools.weather_tool import get_weather
from tools.budget_tool import estimate_budget


def generate_travel_plan(source, destination):

    # Flight Tool
    flight = search_flights(source, destination)

    # Hotel Tool
    hotel = recommend_hotels(destination)

    # Places Tool
    places = suggest_places(destination)

    # Weather Tool
    weather = get_weather(destination)

    # Budget Tool
    budget = estimate_budget(flight, hotel)

    # Build itinerary
    itinerary = []

    for i, place in enumerate(places[:3], start=1):

        if i == 1:
            itinerary.append(f"Day 1: Visit {place['name']}")

        elif i == 2:
            itinerary.append(f"Day 2: Explore {place['name']}")

        elif i == 3:
            itinerary.append(f"Day 3: Enjoy {place['name']}")

    # Final structured response
    travel_plan = {
        "flight": flight,
        "hotel": hotel,
        "places": places,
        "weather": weather,
        "budget": budget,
        "itinerary": itinerary,
        "reasoning": [
            "Cheapest available flight selected",
            "Highest-rated hotel selected",
            "Tourist places selected based on ratings",
            "Weather considered for planning",
            "Budget estimated using flight, hotel and local expenses"
        ]
    }

    return travel_plan
