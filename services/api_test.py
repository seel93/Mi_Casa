import requests
from datetime import datetime
from dao import weather_summary, location_forecast
from services import strava_service, weather_service, snowdepth_service, avalanche_service
from config import yr_constants


def yr_test_api_health():
    res = requests.get('https://api.met.no/weatherapi/locationforecast/2.0/healthz',
                       headers=yr_constants.YR_HEADERS)


def yr_test_location(payload_lat_lon):
    location = weather_service.yr_location_summary(payload_lat_lon).get('properties').get('timeseries')
    summary = weather_summary.WeatherSummary(**location[0].get('data').get('next_12_hours').get('summary'))
    details = weather_summary.WeatherDetails(**location[0].get('data').get('next_12_hours').get('details'))
    response = {
        'symbol': summary.symbol_code,
        'confidence': summary.symbol_confidence,
        'probability': details.probability_of_precipitation
    }

    return response


def yr_multiple_location_test(payload_list_lat_lon):
    weather_service.yr_multiple_locations_summary(payload_list_lat_lon)


def yr_location_forecast_test(location_id):
    location_forecast_response = weather_service.yr_location_forecast(location_id).get('dayIntervals')

    forecast_list = []

    for i in location_forecast_response:
        forecast_list.append(
            location_forecast.LocationForecast(
                dayInterval=location_forecast.DayInterval(
                    datetime.strptime(i.get('start'),
                                      '%Y-%m-%dT%H:%M:%S%z').date(),
                    datetime.strptime(i.get('end'),
                                      '%Y-%m-%dT%H:%M:%S%z').date(),
                    i.get('twentyFourHourSymbol'),
                    i.get('symbolConfidence')
                ),
                precipitation=location_forecast.Precipitation(**i.get('precipitation')),
                temperature=location_forecast.Temperature(**i.get('temperature')),
                wind=location_forecast.Wind(**i.get('wind'))
            )
        )


def yr_snow_test():
    snowdepth_service.get_snow_depths_for_region(yr_constants.ROMSDALEN_ID)


def avalanche_test():
    avalanche_service.get_report_last_week()


def get_athlete_test():
    strava_service.get_athlete()


def get_activity_test():
    print(strava_service.get_activity(6312456143))


def get_activities_test():
    strava_service.get_activities()
