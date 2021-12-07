from services import weather_service
from services import yr_constants
import requests


def yr_test_api_health():
    res = requests.get('https://api.met.no/weatherapi/locationforecast/2.0/healthz', headers=yr_constants.yr_headers)
    print(res.content)


def yr_test_location(payload_lat_lon):
    weather_service.yr_location(payload_lat_lon)


def yr_multiple_location_test(payload_list_lat_lon):
    weather_service.yr_multiple_locations(payload_list_lat_lon)
