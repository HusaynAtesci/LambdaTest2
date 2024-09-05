import json
import requests

def fetch_weather_data(event, context):
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

        # Prepare response body with extracted fields
        body = {
            "message": "Weather data fetched successfully!",
            "temperature_c": temperature,
            "humidity_percent": humidity,
            "wind_speed_kph": wind_speed,
            "condition": condition,
            "uv_index": uv_index
        }

        # Return a successful response
        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

    except requests.exceptions.RequestException as e:
        # Handle errors during the API request
        body = {
            "message": "Error fetching data from WeatherAPI",
            "error": str(e)
        }
        response = {
            "statusCode": 500,
            "body": json.dumps(body)
        }

    return response
