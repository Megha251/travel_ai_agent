from tools.flight_tool import search_flights
from tools.hotel_tool import recommend_hotels
from tools.places_tool import suggest_places
from tools.weather_tool import get_weather
from tools.budget_tool import estimate_budget

source = input("Enter Source City: ")
destination = input("Enter Destination City: ")

print("\nAI Travel Planning Assistant\n")

# Flights
print("Flight Details")
flight = search_flights(source, destination)
print(flight)

# Hotels
print("\nHotel Details")
hotel = recommend_hotels(destination)
print(hotel)

# Places
print("\nTop Tourist Places")
places = suggest_places(destination)
print(places)

# Weather
print("\nWeather Information")
weather = get_weather()
print(weather)

# Budget
if isinstance(flight, dict) and isinstance(hotel, dict):

    print("\nEstimated Budget")

    budget = estimate_budget(flight, hotel)

    print(budget)