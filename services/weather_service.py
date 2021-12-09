import requests
import logging
from config import yr_constants


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
