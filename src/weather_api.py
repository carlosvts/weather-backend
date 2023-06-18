import os

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "http://api.weatherapi.com/v1/current.json"

api_key = os.getenv("API-KEY")

# Obrigatory params
params = {
    "q": "Belo Horizonte",
    "key": api_key,
    "lang": "pt",  # Optional
}

response = requests.get(BASE_URL, params=params)
