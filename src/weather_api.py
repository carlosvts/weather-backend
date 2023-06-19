import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from requests import Response

import requests
from dotenv import load_dotenv
from requests import HTTPError

load_dotenv()

api_key = os.getenv("API-KEY")


class WeatherAPI():
    def __init__(self, api_key, base_url="http://api.weatherapi.com/v1/"):
        self.api_key = api_key
        self.BASE_URL = base_url

    def set_endpoint(self, api_method: str):
        return self.BASE_URL + api_method

    def http_issuccess(self, response: 'Response'):
        if response.status_code != 200:
            raise HTTPError(
                "Erro ao conectar-se com a API, status code:",
                response.status_code
            )

    def get_current_weather(self, q: str, lang: str | None = "pt"):
        api_endpoint_url = self.set_endpoint("current.json")

        _params = {
            "q": q,
            "key": api_key,
            "lang": lang,
        }
        response = requests.get(api_endpoint_url, params=_params)
        self.http_issuccess(response)

        return response

    def get_forecast(self, q: str, days: str, lang: str | None = "pt"):
        api_endpoint_url = self.set_endpoint("forecast.json")

        _params = {
            "q": q,
            "key": api_key,
            "days": days,
            "lang": lang,  # Optional
        }

        response = requests.get(api_endpoint_url, params=_params)
        self.http_issuccess(response)

        return response

    def current_weather_general_response(self, response: 'Response'):
        """
        Base general response for the user
        """
        return (
            f"Na cidade de {response.json()['location']['name']} da região de "
            f"{response.json()['location']['region']} - "
            f"{response.json()['location']['country']}, "
            f"a temperatura é de {response.json()['current']['temp_c']}℃, com "
            "sensação térmica de "
            f"{response.json()['current']['feelslike_c']}℃ "
            "Além disso, a cidade está na condição de"
            f"{response.json()['current']['condition']['text']}"
            f"a velocidade dos ventos na região é de aproximadamente "
            f"{response.json()['current']['wind_kph']} quilômetros por hora"
        )

    def current_weather_specific_response(
            self, response: 'Response', response_option: str | None
    ):
        """
        Show specific responses based on user input, if user didnt specified,
        show general response
        """
        if response_option is None:
            return self.current_weather_general_response(response)

        if response_option == "T":
            return (print(
                f"A temperatura na cidade "
                f"de {response.json()['location']['name']} "
                f"é de {response.json()['current']['temp_c']}℃ com "
                "sensação térmica de "
                f"{response.json()['current']['feelslike_c']}℃"
            ))
        if response_option == "V":
            return (print(
                f"Os ventos na cidade de {response.json()['location']['name']}"
                " Estão com uma velocidade de "
                f"{response.json()['current']['wind_kph']} km/h"
            ))
        if response_option == "H":
            return (print(
                f"{response.json()['location']['localtime']} é o horario da "
                f"cidade de {response.json()['location']['name']} "
            ))
        if response_option == "L":
            return (print(
                f"A cidade de {response.json()['location']['name']} "
                "se localiza na "
                f"região de {response.json()['location']['region']} - "
                f"{response.json()['location']['country']}, "
                f"na latitude de {response.json()['location']['lat']}"
            ))
