import streamlit as st

from tools.flight_tool import search_flights
from tools.hotel_tool import recommend_hotels
from tools.places_tool import suggest_places
from tools.weather_tool import get_weather
from tools.budget_tool import estimate_budget


# Page Config
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="centered"
)

# Title
st.title("✈️ AI Travel Planning Assistant")

st.write(
    "Plan your trip with flights, hotels, tourist places, "
    "weather updates, and budget estimation."
)

# User Input
source = st.text_input("Enter Source City")

destination = st.text_input("Enter Destination City")


# Button
if st.button("Generate Travel Plan"):

    # Empty Validation
    if source.strip() == "" or destination.strip() == "":

        st.error("Please enter both source and destination cities.")

    else:

        try:

            # Flight Search
            flight = search_flights(source, destination)

            # Hotel Recommendation
            hotel = recommend_hotels(destination)

            # Places Suggestion
            places = suggest_places(destination)

            # Weather Information
            weather = get_weather(destination)

            # Budget Estimation
            budget = estimate_budget(flight, hotel)

            # Trip Heading
            st.subheader(f"🧳 Trip Plan: {source} ➜ {destination}")

            # ---------------------------------------------------
            # Flight Section
            # ---------------------------------------------------

            st.subheader("✈️ Flight Details")

            # If direct route not found
            if (
                flight["from"].lower() != source.lower()
                or flight["to"].lower() != destination.lower()
            ):

                st.warning(
                    f"No direct route found from {source} "
                    f"to {destination}. "
                    f"Showing cheapest available route instead."
                )

            st.write(f"**Airline:** {flight['airline']}")

            st.write(f"**From:** {flight['from']}")

            st.write(f"**To:** {flight['to']}")

            st.write(
                f"**Departure:** {flight['departure_time']}"
            )

            st.write(
                f"**Arrival:** {flight['arrival_time']}"
            )

            st.success(
                f"💸 Flight Price: ₹{flight['price']}"
            )

            # ---------------------------------------------------
            # Hotel Section
            # ---------------------------------------------------

            st.subheader("🏨 Hotel Recommendation")

            st.write(f"**Hotel Name:** {hotel['name']}")

            st.write(f"**City:** {hotel['city']}")

            st.write(f"**Stars:** ⭐ {hotel['stars']}")

            st.write(
                f"**Price Per Night:** ₹{hotel['price_per_night']}"
            )

            st.write(
                f"**Amenities:** {', '.join(hotel['amenities'])}"
            )

            # ---------------------------------------------------
            # Places Section
            # ---------------------------------------------------

            st.subheader("📍 Top Tourist Places")

            for place in places:

                st.write(
                    f"**{place['name']}** "
                    f"({place['type']}) ⭐ {place['rating']}"
                )

            # ---------------------------------------------------
            # Weather Section
            # ---------------------------------------------------

            st.subheader("🌤️ Weather Information")

            st.write(
                f"🌡️ Temperature: "
                f"{weather['temperature']} °C"
            )

            st.write(
                f"💨 Wind Speed: "
                f"{weather['windspeed']} km/h"
            )

            st.write(
                f"🕒 Time: {weather['time']}"
            )

            # ---------------------------------------------------
            # Itinerary Section
            # ---------------------------------------------------

            st.subheader("🗓️ Suggested 3-Day Itinerary")

            if len(places) >= 3:

                st.write(
                    f"Day 1: Visit {places[0]['name']}"
                )

                st.write(
                    f"Day 2: Explore {places[1]['name']}"
                )

                st.write(
                    f"Day 3: Enjoy {places[2]['name']}"
                )

            # ---------------------------------------------------
            # Budget Section
            # ---------------------------------------------------

            st.subheader("💰 Budget Estimation")

            st.write(
                f"✈️ Flight Cost: ₹{budget['flight_cost']}"
            )

            st.write(
                f"🏨 Hotel Cost: ₹{budget['hotel_cost']}"
            )

            st.write(
                f"🍽️ Food & Local Travel: "
                f"₹{budget['food_and_travel']}"
            )

            st.success(
                f"✅ Total Estimated Budget: "
                f"₹{budget['total_cost']}"
            )

            # ---------------------------------------------------
            # Reasoning Section
            # ---------------------------------------------------

            st.subheader("🧐 Why These Recommendations?")

            st.write(
                "• Cheapest available flight selected"
            )

            st.write(
                "• Highest-rated hotel selected"
            )

            st.write(
                "• Tourist places selected based on ratings"
            )

            st.write(
                "• Weather considered for planning"
            )

            st.write(
                "• Budget estimated using flight, "
                "hotel and local expenses"
            )

            # Final Message
            st.success(
                f"🎉 Your trip from {source} "
                f"to {destination} is ready!"
            )

        except Exception as e:

            st.error(f"Error: {e}")