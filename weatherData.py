import requests

def fetch_weather_data(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    api_key = "27395c79e1e29b821b34565f3c6ca3f2"
    city = "London"
    weather_data = fetch_weather_data(api_key, city)
    if weather_data:
        print(weather_data)
    else:
        print("Failed to fetch weather data")