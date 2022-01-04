import requests
from datetime import datetime, timedelta
import logging
from config import varsom_constants, yr_constants
from dao import avalanche_forecast
from itertools import groupby


def get_report_last_week(lat_lon):
    now = datetime.now().strftime('%y.%m.%d')
    before = datetime.today() - timedelta(days=7)
    before = before.strftime('%y.%m.%d')
    try:
        return requests.get(
            f'{varsom_constants.API_URL}/AvalancheWarningByCoordinates/Simple/{lat_lon[0]}/{lat_lon[1]}/1/{before}/{now}'
        ).json()
    except requests.exceptions.HTTPError as err:
        logging.error(
            f'{varsom_constants.API_URL}/AvalancheWarningByCoordinates/Simple/{lat_lon[0]}/{lat_lon[1]}/1/{before}/{now} failed: {err}')
        raise SystemExit(err)


def group_report_by_danger(avy_report_list):
    dangers = []
    return [dangers for key, result in groupby(
        avy_report_list, key=lambda danger: avy_report_list.DangerLevel
    )]