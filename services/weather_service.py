import requests
import logging
from config import yr_constants
from dao import location_forecast
from dao.location_forecast import LocationForecast


def check_api_health():
    try:
        return requests.get(f'{yr_constants.YR_API_URL}/health').status_code == '200'
    except requests.exceptions.HTTPError as err:
        logging.error(f'yr api not available: {err}')
        raise SystemExit(err)


def yr_location_summary(payload_lat_lon):
    try:
        payload = {'lat': payload_lat_lon[0], 'lon': payload_lat_lon[1]}
        res = requests.get('https://api.met.no/weatherapi/locationforecast/2.0/complete',
                           headers=yr_constants.YR_HEADERS,
                           params=payload
                           )
        return res.json()
    except requests.exceptions.HTTPError as err:
        logging.error(f'yr location summary failed: {err}')
        raise SystemExit(err)


def yr_multiple_locations_summary(location_list):
    weather_data = []
    for i in location_list:
        weather_data.append(yr_location_summary(location_list[0]))
    return weather_data


def yr_location_forecast(location_id):
    try:
        return requests.get(f'{yr_constants.YR_API_URL}/locations/{location_id}/forecast',
                            headers=yr_constants.YR_HEADERS
                            ).json()
    except requests.exceptions.HTTPError as err:
        logging.error(f'{yr_constants.YR_API_URL}/locations/{location_id}/forecast failed: {err}')
        raise SystemExit(err)


def check_for_snow(location_id):
    return filter(find_days_with_snow, [location_forecast.LocationForecast.from_dict(x) for x in
                                        yr_location_forecast(location_id).get('dayIntervals')])


def find_days_with_snow(forecast: LocationForecast):
    logging.info(forecast.temperature.max)
    return forecast.precipitation.value > 0.5 \
           and forecast.precipitation.probability >= 50 \
           and forecast.wind.max < 15 \
           and forecast.temperature.max < 1.0
