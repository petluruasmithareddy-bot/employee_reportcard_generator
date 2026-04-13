import streamlit as st
import requests

st.title("🌦️ Weather App")

city = st.text_input("Enter city name")

api_key = "adea292b36c4f7f215ed8e1bcce9618a"

if st.button("Get Weather"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if str(data["cod"]) == "200":
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather = data["weather"][0]["description"]

            st.success(f"City: {city}")
            st.success(f"Temperature: {temp}°C")
            st.success(f"Humidity: {humidity}%")
            st.success(f"Condition: {weather}")
        elif str(data["cod"]) == "401":
            st.error("Invalid API Key")
        else:
            st.error("City not found")

    except Exception as e:
        st.error(f"Error: {e}")