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

    def get_forecast(self, q: str, hour, lang: str | None = None):
        api_endpoint_url = self.set_api_endpoint("forecast.json")

        _params = {
            "q": q,
            "key": api_key,
            "days": 2,  # 1(current day) + 1 = next day in this api
            "lang": lang,  # Optional
            "hour": hour,  # Optional
        }

        response = requests.get(api_endpoint_url, params=_params)
        self.http_issuccess(response)
        return response

    def current_weather_general_response(self, response: 'Response'):
        """
        Base general response for the user
        """
        city = response.json()['location']['name']
        location = response.json()['location']
        current = response.json()['current']
        return (
            f"In the city of {city}"
            "in the region of "
            f"{location['region']} - "
            f"{location['country']}, "
            f"the temperature is {current['temp_c']}°C, "
            "with a feels-like temperature of "
            f"{current['feelslike_c']}°C. "
            "Additionally, the city is experiencing"
            f"{current['condition']['text']}. "
            "The wind speed in the region is approximately "
            f"{current['wind_kph']} kilometers per hour."
        )

    def realtime_specific_response(
            self, response: 'Response', response_option: str | None
    ):
        """
        Show specific responses based on user input, if user didnt specified,
        show general response
        """

        city = response.json()['location']['name']
        location = response.json()['location']
        current = response.json()['current']
        if response_option is None:
            return self.current_weather_general_response(response)

        if response_option == "T":
            print(
                "The temperature in the city of "
                f"{city} "
                f"is {current['temp_c']}°C "
                "with a feels-like temperature of "
                f"{current['feelslike_c']}°C."
            )

        if response_option == "W":
            print(
                f"The winds in the city of {city} "
                "are blowing at a speed of "
                f"{current['wind_kph']} km/h."
            )

        if response_option == "H":
            print(
                f"{location['localtime']} "
                "is the local time in "
                f"the city of {city}."
            )

        if response_option == "L":
            print(
                f"The city of {city} "
                "is located in "
                f"the region of {location['region']} - "
                f"{location['country']}, "
                f"at a latitude of {location['lat']}."
            )

    def forecast_response(
            self, response: 'Response', response_option: str, hour: str):

        city = response.json()['location']['name']

        forecast_date = response.json()['forecast']['forecastday'][1]['date']
        # Forecast
        forecast_day_data = response.json(
        )['forecast']['forecastday'][0]['day']

        max_temp_celsius = forecast_day_data['maxtemp_c']

        min_temp_celsius = forecast_day_data['mintemp_c']

        max_wind_velocity = forecast_day_data['maxwind_kph']

        chance_rain = forecast_day_data['daily_chance_of_rain']

        # Forecast in the specific Hour
        hour_forecast_data = response.json(
        )['forecast']['forecastday'][0]['hour'][0]

        hour_temp = hour_forecast_data['temp_c']
        hour_feels_like_celsius = hour_forecast_data['feelslike_c']
        hour_wind_velocity = hour_forecast_data['wind_kph']
        hour_chance_rain = hour_forecast_data['chance_of_rain']

        if response_option == "T":
            print("DAY", forecast_date)
            print(  # Forecast Day
                f"In the city of {city} "
                "the max temperature of the day is "
                f"{max_temp_celsius}°C and the min is "
                f"{min_temp_celsius}°C."
            )
            print(  # Hour
                f"At {hour} hours, "
                f"the temperature is {hour_temp}°C with a feels-like temp of "
                f"{hour_feels_like_celsius}"
            )

        if response_option == "W":
            print("DAY", forecast_date)
            print(
                f"In the city of {city} "
                f"the winds are blowing at a max speed of {max_wind_velocity}"
                "kp/h"
            )
            print(
                f"At {hour} hours, "
                f"the winds are blowing at {hour_wind_velocity}kp/h"
            )

        if response_option == "R":
            print("DAY", forecast_date)
            print(
                f"The chance of rain in the city of {city} is {chance_rain}%"
            )
            print(f"At {hour} hours, "
                  f"the chance of rain is {hour_chance_rain}%")
