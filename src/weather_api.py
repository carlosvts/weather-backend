import os

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "http://api.weatherapi.com/v1"

api_key = os.getenv("API-KEY")

params = {
    "key": api_key
}

response = requests.get(BASE_URL, params=params)
