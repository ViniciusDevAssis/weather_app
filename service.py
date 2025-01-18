import requests

def get_coordinate_by_name(api_key, city, country, limit=1):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{country}&limit={limit}&appid={api_key}"
    request = requests.get(url).json()
    return request[0]["lat"], request[0]["lon"]

def get_user_location_by_ip():
    url = f"https://ipinfo.io/"
    request = requests.get(url).json()
    return request['loc'].split(',')

def get_weather_by_city(api_key, city, country):
    lat, lon = get_coordinate_by_name(api_key, city, country)
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    request = requests.get(url).json()
    return request['weather'][0]

def get_weather_forecast_by_city(api_key, city, country):
    lat, lon = get_coordinate_by_name(api_key, city, country)
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"
    request = requests.get(url).json()
    return request

api_key = "f43a4f52de76138fa859889f6dfa4f65"
city = "Feira de Santana"
country = "BR"

print(get_weather_forecast_by_city(api_key, city, country))
