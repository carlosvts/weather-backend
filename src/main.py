from utils import (current_weather_localization_input, days_input, user_input,
                   weather_response_options)
from weather_api import WeatherAPI, api_key

# o que voce gostaria de fazer
# forecast ou current
# uma func pra cada opção
# essa func pede os dados e passa eles para a WeatherAPI, essa mesma func
# retorna as informações com um texto f" formatadin

user_option = user_input()
location = current_weather_localization_input()

weatherapi = WeatherAPI(api_key)

if user_option == "1":
    response = weatherapi.get_current_weather(location)
    response_options = weather_response_options(location)
    weatherapi.current_weather_specific_response(response, response_options)

if user_option == "2":
    days = days_input()
    response = weatherapi.get_forecast(location, days=days)
