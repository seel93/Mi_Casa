import requests
from datetime import datetime
from dao import weather_summary, location_forecast, avalanche_forecast, snow_depth
from services import strava_service, weather_service, snowdepth_service, avalanche_service
from config import yr_constants
import logging


def yr_test_api_health():
    res = requests.get('https://api.met.no/weatherapi/locationforecast/2.0/healthz',
                       headers=yr_constants.YR_HEADERS)


def yr_test_location(payload_lat_lon):
    location = weather_service.yr_location_summary(payload_lat_lon).get('properties').get('timeseries')
    return location_forecast.LocationSummary.from_dict(location[0])


def yr_multiple_location_test(payload_list_lat_lon):
    weather_service.yr_multiple_locations_summary(payload_list_lat_lon)


def yr_location_forecast_test(location_id):
    return [location_forecast.LocationForecast.from_dict(x) for x in weather_service.yr_location_forecast(location_id).get('dayIntervals')]


def find_snowy_days(location_id):
    return list(weather_service.check_for_snow(location_id))


def yr_snow_test():
    print(snowdepth_service.get_snow_depths_for_region(yr_constants.ROMSDALEN_ID))


def avalanche_test(report):
    return avalanche_forecast.AvalancheReport.from_dict(report)


def map_res_avy(lat_lon):
    for report in map(avalanche_test, [avalanche_forecast.AvalancheReport.from_dict(i) for i in avalanche_service.get_report_last_week(lat_lon)]):
        print(report)


def get_athlete_test():
    strava_service.get_athlete()


def get_activity_test():
    print(strava_service.get_activity(6312456143))


def get_activities_test():
    strava_service.get_activities()
