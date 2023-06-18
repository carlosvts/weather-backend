import os

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

    def get_current_weather(self, q: str, lang: str | None = None):
        api_endpoint_url = self.set_endpoint("current.json")

        _params = {
            "q": q,
            "key": api_key,
            "lang": lang,
        }
        response = requests.get(api_endpoint_url, params=_params)
        self.http_issuccess(response)

    def get_forecast(self, q: str, days: str, lang: str | None = None):
        api_endpoint_url = self.set_endpoint("forecast.json")

        _params = {
            "q": q,
            "key": api_key,
            "days": days,
            "lang": lang,  # Optional
        }

        response = requests.get(api_endpoint_url, params=_params)
        self.http_issuccess(response)
