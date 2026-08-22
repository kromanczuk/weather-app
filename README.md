# Weather checker

Fetches current weather and a one-day forecast for a city via a Streamlit web app.

## Python version

This project was built with **Python 3.14.5**.

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add your [OpenWeatherMap](https://openweathermap.org/api) API key. Create `.streamlit/secrets.toml` with:

```toml
OPENWEATHER_API_KEY = "your_key_here"
```

## Run the web app

With your virtual environment activated, run:

```bash
streamlit run app.py
```

Streamlit opens the app in your browser. Enter a city name (e.g. `London` or `New York`) to see the current temperature and conditions, plus a line chart of the forecast for the next 24 hours.
