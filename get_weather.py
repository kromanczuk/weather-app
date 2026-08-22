import requests
import streamlit as st

API_KEY = st.secrets["OPENWEATHER_API_KEY"]

def get_weather(cityName) -> None:
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": cityName,
        "APPID": API_KEY,
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
    return city_name, temp, description




def get_one_day_timeline(cityName: str) -> list:
    timelineUrl = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
    "q": cityName,
    "APPID": API_KEY,
    "units": "metric"
    }

    try:
        response = requests.get(timelineUrl, params=params)
        response.raise_for_status()
        data = response.json()
    except requests.HTTPError as e:
        print(f"Returned HTTP error: {e}")
        return

    return data['list']




def get_city() -> str:
    city = input("Please provide a city name that you'd like to check: " )
    print(f'All set! Checking for "{city}"')
    return city

if __name__ == "__main__":
    city = get_city()
    get_weather(city)
