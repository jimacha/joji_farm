import requests

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "34a10f8c7e74fc9b506a7dc4b84c751a
": api_key,  # Replace with your API key from OpenWeatherMap
        "units": "metric",  # You can change the units to 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print("Error: Unable to fetch weather data")
        return None

if __name__ == "__main__":
    city = "New York"  # Replace with the city name you want to get weather data for
    api_key = "34a10f8c7e74fc9b506a7dc4b84c751a
"

    weather_data = get_weather(city, api_key)

    if weather_data:
        print(f"Weather in {city}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
    else:
        print("Weather data not available.")
