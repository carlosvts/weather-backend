import os
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from requests import Response

from pprint import pprint

import requests
from dotenv import load_dotenv
from requests import HTTPError

load_dotenv()

api_key = os.getenv("API-KEY")


class WeatherAPI():
    def __init__(self, api_key, base_url="http://api.weatherapi.com/v1/"):
        self.api_key = api_key
        self.BASE_URL = base_url

    def set_api_endpoint(self, api_method: str):
        return self.BASE_URL + api_method

    def http_issuccess(self, response: 'Response'):
        if response.status_code != 200:
            raise HTTPError(
                "Can't connect with API, status code:",
                response.status_code
            )

    def get_current_weather(self, q: str, lang: str | None = None):
        api_endpoint_url = self.set_api_endpoint("current.json")

        _params = {
            "q": q,
            "key": api_key,
            "lang": lang,
        }
        response = requests.get(api_endpoint_url, params=_params)
        self.http_issuccess(response)

        return response

    def get_forecast(self, q: str, days, hour, lang: str | None = None):
        api_endpoint_url = self.set_api_endpoint("forecast.json")

        _params = {
            "q": q,
            "key": api_key,
            "days": days,
            "lang": lang,  # Optional
            "hour": hour,  # Optional
        }

        response = requests.get(api_endpoint_url, params=_params)
        self.http_issuccess(response)
        pprint(response.text)
        return response

    def current_weather_general_response(self, response: 'Response'):
        """
        Base general response for the user
        """
        return (
            f"In the city of {response.json()['location']['name']}"
            "in the region of "
            f"{response.json()['location']['region']} - "
            f"{response.json()['location']['country']}, "
            f"the temperature is {response.json()['current']['temp_c']}°C, "
            "with a feels-like temperature of "
            f"{response.json()['current']['feelslike_c']}°C. "
            "Additionally, the city is experiencing"
            f"{response.json()['current']['condition']['text']}. "
            "The wind speed in the region is approximately "
            f"{response.json()['current']['wind_kph']} kilometers per hour."
        )

    def realtime_specific_response(
            self, response: 'Response', response_option: str | None
    ):
        """
        Show specific responses based on user input, if user didnt specified,
        show general response
        """
        if response_option is None:
            return self.current_weather_general_response(response)

        if response_option == "T":
            print(
                "The temperature in the city of "
                f"{response.json()['location']['name']} "
                f"is {response.json()['current']['temp_c']}°C "
                "with a feels-like temperature of "
                f"{response.json()['current']['feelslike_c']}°C."
            )
            return
        if response_option == "W":
            print(
                "The winds in the city of "
                f"{response.json()['location']['name']} "
                "are blowing at a speed of "
                f"{response.json()['current']['wind_kph']} km/h."
            )
            return
        if response_option == "H":
            print(
                f"{response.json()['location']['localtime']} "
                "is the local time in "
                f"the city of {response.json()['location']['name']}."
            )
            return
        if response_option == "L":
            print(
                f"The city of {response.json()['location']['name']}"
                "is located in "
                f"the region of {response.json()['location']['region']} - "
                f"{response.json()['location']['country']}, "
                f"at a latitude of {response.json()['location']['lat']}."
            )
            return

    def forecast_general_response(
            self, response: 'Response', response_option: str | None):
        ...

    def forecast_specific_response(
            self, response: 'Response', response_option: str | None):

        if response_option == "T":
            print("The temperature in the city of "
                  f"{response.json()['location']['name']} "
                  f"is {response.json()['current']['temp_c']}°C "
                  "with a feels-like temperature of "
                  f"{response.json()['current']['feelslike_c']}°C."
                  )
        if response_option == "W":
            ...

        if response_option == "R":
            ...
