import os
from pprint import pprint
from typing import TYPE_CHECKING
if TYPE_CHECKING:
from requests import Response
import requests
from dotenv import load_dotenv
from requests import HTTPError, Response

load_dotenv()

api_key = os.getenv("API-KEY")


class WeatherAPI():
    def __init__(self, api_key, base_url="http://api.weatherapi.com/v1/"):
        self.api_key = api_key
        self.BASE_URL = base_url

    def set_endpoint(self, api_method: str):
        return self.BASE_URL + api_method

    def http_issuccess(self, response: Response):
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

        pprint(response.json())
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

    def weather_general_response(self, response: Response):
        f"Na cidade de {response.json()['location']['name']} da região de "
        f"{response.json()['location']['region']} - "
        f"{response.json()['location']['country']}, "
        f"a temperatura é de {response.json()['current']['temp_c']}℃, com "
        "sensação térmica de "
        f"{response.json()['current']['feelslike_c']}℃ "
        "Além disso, a velocidade dos ventos na região é de aproximadamente "
        f"{response.json()['current']['wind_kph']} quilômetros por hora"
    
    def weather_specific_response(self, response: Response, response_type):
