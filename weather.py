import requests
import pandas as pd
from datetime import date

# MY camping location
lattitude = -51.000000
longitude = -73.000000
location = "Patagonia"

#camping month and day range
month = 12
start_day = 1
end_day = 15

def get_historical_weather(lat, lon, start_date, end_date):
  url = "https://archive-api.open-meteo.com/v1/archive"
  params = {
      "latitude": lat,
      "longitude": lon,
      "start_date": start_date,
      "end_date": end_date,
      "daily": "temperature_2m_max,temperature_2m_min",
      "timezone": "America/Los_Angeles"
  }

  response = requests.get(url, params = params)
  return response.json()
