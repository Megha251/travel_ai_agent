import requests


def get_weather(city):

    latitude = 28.6139
    longitude = 77.2090

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}"
        f"&longitude={longitude}"
        f"&current_weather=true"
    )

    response = requests.get(url)

    data = response.json()

    return data["current_weather"]