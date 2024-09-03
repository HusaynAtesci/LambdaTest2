import json
import requests

def fetch_weather_data():
    # WeatherAPI.com endpoint and API key
    api_key = '88a5bc844ef14a278f1162851243108'
    city = 'Amsterdam'
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'

    try:
        # Fetch weather data
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse JSON response
        weather_data = response.json()

        # Extract required fields
        temperature = weather_data['current']['temp_c']
        humidity = weather_data['current']['humidity']
        wind_speed = weather_data['current']['wind_kph']
        condition = weather_data['current']['condition']['text']
        uv_index = weather_data['current']['uv']

        # Print extracted fields to verify
        print(f"Temperature (C): {temperature}")
        print(f"Humidity (%): {humidity}")
        print(f"Wind Speed (kph): {wind_speed}")
        print(f"Condition: {condition}")
        print(f"UV Index: {uv_index}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from WeatherAPI: {e}")

if __name__ == "__main__":
    fetch_weather_data()
