import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from get_weather import get_one_day_timeline, get_weather



st.title('Get weather for a city!')
st.write('Please type city name:')
city = st.text_input("City", key="city")
test = type(city)

if(city):
    temp, city_name, description  = get_weather(city)
    forecast = get_one_day_timeline(city)
    df = pd.DataFrame({'time': entry['dt_txt'], 'temp': entry['main']['temp']} for entry in forecast)
    st.header('Current weather:')
    st.write(f"It is {temp}°C in {city_name} with {description}.")
    st.header('Forecast:')
    st.line_chart(df.set_index("time"))
