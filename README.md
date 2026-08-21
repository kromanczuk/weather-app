# Weather checker

Small script that asks for a city and prints the current temperature and conditions.

## Setup

1. Create a virtual env and install deps:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Copy `.env_example` to `.env` and add your [OpenWeatherMap](https://openweathermap.org/api) API key:

```
OPENWEATHER_API_KEY=your_key_here
```

## Run

```bash
python get_weather.py
```

It'll prompt you for a city name.  Type something like `London` or `New York` and hit enter.
