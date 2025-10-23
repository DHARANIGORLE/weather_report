import requests
import json

def get_weather(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data):
    if data['cod'] == 200:  # Check if the request was successful
        main = data['main']
        weather = data['weather'][0]

        city = data['name']
        temperature = main['temp']
        humidity = main['humidity']
        description = weather['description']

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
    else:
        print(f"Error: {data['message']}")

def main():
    api_key = '2e2a2627c18aab5927a04d916e3d2f4f'  # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")
    
    weather_data = get_weather(api_key, city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
