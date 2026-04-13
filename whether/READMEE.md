🌦️ Weather App using API (Streamlit + Python)
 Overview

This project is a simple and interactive Weather Application built using Python. It fetches real-time weather data from the OpenWeatherMap API and displays it using a user-friendly Streamlit UI.

 Features
 Get real-time weather data for any city
 Displays temperature in Celsius
 Shows humidity levels
 Displays weather condition (clear, cloudy, rain, etc.)
 Error handling for invalid city or API key
 Interactive web-based UI using Streamlit
🛠️ Technologies Used
Python 
Streamlit (for UI)
Requests (for API calls)
JSON (for handling API response data)
 Project Structure
weather_app/
│
├── app.py              # Streamlit UI code
├── weather_logic.py    # (Optional) reusable logic file
├── terminal_app.py     # (Optional) terminal version
└── README.md
⚙️ Installation & Setup
1️ Clone the repository
git clone https://github.com/your-username/weather-app.git
cd weather-app
2️ Create Virtual Environment (optional but recommended)
python -m venv .venv
.venv\Scripts\activate   # Windows
3️ Install dependencies
pip install streamlit requests
 API Key Setup
Go to OpenWeatherMap
Sign up and generate your API key
Replace in code:
api_key = "YOUR_API_KEY"

 Note: API key may take a few minutes to activate.

▶️ How to Run
🌐 Run Streamlit UI
streamlit run app.py

👉 Open in browser:
http://localhost:8501

💻 Run Terminal Version (optional)
python terminal_app.py
🧠 How It Works
User enters a city name
Application sends request to API using requests
API returns data in JSON format
Required data (temperature, humidity, condition) is extracted
Results are displayed in UI
📊 Sample Output
City: Hyderabad
Temperature: 32°C
Humidity: 60%
Condition: clear sky
