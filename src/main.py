from utils import (current_weather_localization_input, user_input,
                   weather_response_options)
from weather_api import WeatherAPI, api_key

# o que voce gostaria de fazer
# forecast ou current
# uma func pra cada opção
# essa func pede os dados e passa eles para a WeatherAPI, essa mesma func
# retorna as informações com um texto f" formatadin

user_option = user_input()

if user_option == "1":
    weather = WeatherAPI(api_key)
    location = current_weather_localization_input()
    response = weather.get_current_weather(location)
    response_options = weather_response_options(location)
    weather.current_weather_specific_response(response, response_options)
