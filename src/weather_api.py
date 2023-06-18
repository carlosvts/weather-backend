import os

import requests
from dotenv import load_dotenv
from requests import HTTPError, Response

load_dotenv()

api_key = os.getenv("API-KEY")

BASE_URL = "http://api.weatherapi.com/v1/"


def set_endpoint(api_method: str):
    return BASE_URL + api_method


def http_issuccess(response: Response):
    if response.status_code != 200:
        raise HTTPError(
            "Erro ao conectar-se com a API, status code:", response.status_code
        )


def get_current_weather(q: str, lang: str | None = None):
    api_endpoint_url = set_endpoint("current.json")

    _params = {
        "q": q,
        "key": api_key,
        "lang": lang,
    }
    response = requests.get(api_endpoint_url, params=_params)
    http_issuccess(response)


def get_forecast(q: str, days: str, lang: str | None = None):
    api_endpoint_url = set_endpoint("forecast.json")

    _params = {
        "q": q,
        "key": api_key,
        "days": days,
        "lang": lang,  # Optional
    }
    response = requests.get(api_endpoint_url, params=_params)
    http_issuccess(response)
