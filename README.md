🌦️ Weather Information App using OpenWeatherMap API
📌 Overview

This Python project is a simple Weather Information App that fetches and displays real-time weather data for any city using the OpenWeatherMap API.
It provides essential weather details like temperature, humidity, and weather description in an easy-to-read format.

⚙️ Features

✅ Fetches real-time weather data using OpenWeatherMap API
✅ Displays temperature (in °C), humidity, and description
✅ Handles invalid city names and API errors gracefully
✅ Lightweight and beginner-friendly Python script

🧠 How It Works

The user enters a city name.

The program sends an API request to OpenWeatherMap using the requests library.

It retrieves weather data in JSON format.

The script extracts and displays temperature, humidity, and weather conditions.

🧩 Code Explanation
get_weather(api_key, city)

Sends an HTTP request to the OpenWeatherMap API and retrieves weather data in JSON format.

display_weather(data)

Parses the JSON response and displays temperature, humidity, and description.

main()

Handles user input and function calls.

🚀 Installation & Usage
1️⃣ Prerequisites

Make sure you have Python 3.x installed.
Install the required library:

pip install requests

2️⃣ Get Your API Key

Sign up at OpenWeatherMap

Generate a free API key

Replace it in the script:

api_key = 'YOUR_API_KEY'

3️⃣ Run the Script
python weather_app.py

4️⃣ Example Output
Enter city name: Hyderabad
Weather in Hyderabad:
Temperature: 27.23°C
Humidity: 74%
Description: haze

💡 Sample Output Screenshot (Optional)

Add a terminal screenshot of your program output here.

👩‍💻 Author

Gorle Dharani
💼 Passionate about Python, APIs, and Real-world Projects

🏁 Future Enhancements

🔹 Add GUI using Tkinter or Streamlit
🔹 Show 5-day forecast
🔹 Integrate geolocation-based weather detection
