from utils import (current_weather_localization_input,
                   forecast_response_options, hours_input, user_input,
                   weather_response_options)
from weather_api import WeatherAPI, api_key

user_option = user_input()
location = current_weather_localization_input()

weatherapi = WeatherAPI(api_key)

if user_option == "1":
    response = weatherapi.get_current_weather(location)
    response_options = weather_response_options(location)
    weatherapi.realtime_specific_response(response, response_options)

if user_option == "2":
    hour = hours_input()
    response = weatherapi.get_forecast(location, hour=hour)
    response_option = forecast_response_options(location)
    weatherapi.forecast_response(response, response_option, hour)
