def estimate_budget(flight, hotel, days=3):

    flight_cost = flight["price"]

    hotel_cost = hotel["price_per_night"] * days

    food_and_travel = 2000 * days

    total_cost = (
        flight_cost
        + hotel_cost
        + food_and_travel
    )

    return {

        "flight_cost": flight_cost,

        "hotel_cost": hotel_cost,

        "food_and_travel": food_and_travel,

        "total_cost": total_cost
    }