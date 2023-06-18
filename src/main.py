from utils import user_input
from weather_api import WeatherAPI, api_key

# o que voce gostaria de fazer
# forecast ou current
# uma func pra cada opção
# essa func pede os dados e passa eles para a WeatherAPI, essa mesma func
# retorna as informações com um texto f" formatadin

# Receives the option if user wants:
# currently weather info(1) or
# forecast info (2)
user_option = user_input()

if user_option == "1":
    current_weather = WeatherAPI(api_key)
