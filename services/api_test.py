from services import weather_service
from services import yr_constants
from dao import weather_summary
import requests


def yr_test_api_health():
    res = requests.get('https://api.met.no/weatherapi/locationforecast/2.0/healthz', headers=yr_constants.yr_headers)
    print(res.content)


def yr_test_location(payload_lat_lon):
    location = weather_service.yr_location(payload_lat_lon)
    location = location.get('properties').get('timeseries')
    summary = weather_summary.WeatherSummary(**location[0].get('data').get('next_12_hours').get('summary'))
    details = weather_summary.WeatherDetails(**location[0].get('data').get('next_12_hours').get('details'))
    response = {
        'symbol': summary.symbol_code,
        'confidence': summary.symbol_confidence,
        'probability': details.probability_of_precipitation
    }

    return response


def yr_multiple_location_test(payload_list_lat_lon):
    weather_service.yr_multiple_locations(payload_list_lat_lon)
