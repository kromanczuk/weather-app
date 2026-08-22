# Weather checker

Small project that fetches current weather and a one-day forecast for a city. You can use it from the command line or through a Streamlit web app.

## Setup

1. Create a virtual env and install deps:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install streamlit pandas matplotlib numpy
```

2. Copy `.env_example` to `.env` and add your [OpenWeatherMap](https://openweathermap.org/api) API key:

```
OPENWEATHER_API_KEY=your_key_here
```

## Run from the CLI

With your virtual env activated, run:

```bash
python get_weather.py
```

You'll be prompted for a city name. Type something like `London` or `New York` and press Enter. The script fetches weather data from the OpenWeatherMap API.

## Run the Streamlit app

With your virtual env activated, run:

```bash
streamlit run app.py
```

Streamlit opens the app in your browser. Enter a city name in the text box to see the current temperature and conditions, plus a line chart of the forecast for the next 24 hours.
