from services import yr_constants
import requests


def yr_location(payload_lat_lon):
    payload = {'lat': payload_lat_lon[0], 'lon': payload_lat_lon[1]}
    res = requests.get('https://api.met.no/weatherapi/locationforecast/2.0/complete',
                       headers=yr_constants.yr_headers,
                       params=payload
                       )
    return res.json()


def yr_multiple_locations(location_list):
    weather_data = []
    for i in location_list:
        weather_data.append(yr_location(location_list[0]))
    return weather_data
