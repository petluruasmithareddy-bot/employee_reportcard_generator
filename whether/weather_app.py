import requests

city = input("Enter city name: ")
api_key = "adea292b36c4f7f215ed8e1bcce9618a"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

print("DEBUG:", data)   # 👈 Add this to check response

if str(data["cod"]) == "200":
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]

    print(f"\n🌦️ Weather in {city}")
    print(f"Temperature: {temp}°C")
    print(f"Condition: {weather}")
else:
    print("❌ City not found. Please try again.")