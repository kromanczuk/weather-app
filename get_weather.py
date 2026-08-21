import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_wether(cityName) -> None:
    url = "https://api.openweathermap.org/data/2.5/weather"

    print(city)
    params = {
        "q": cityName,
        "appAPI": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
    except requests.HTTPError as e:
        print(f"Returned HTTP error: {e}")
        return

    city_name = data["name"]
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    
    print(f"It is {temp}°C in {city_name} with {description}.")

def get_city() -> str:
    city = input("Please provide a city name that you'd like to check: " )
    print(f'All set! Checking for "{city}"')
    return city

if __name__ == "__main__":
    city = get_city()
    get_wether(city)
