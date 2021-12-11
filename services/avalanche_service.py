import requests
from datetime import datetime, timedelta
import logging
from config import varsom_constants, yr_constants


def get_report_last_week():
    now = datetime.now().strftime('%y.%m.%d')
    before = datetime.today() - timedelta(days=7)
    before = before.strftime('%y.%m.%d')
    try:
        return requests.get(
            f'{varsom_constants.API_URL}/AvalancheWarningByCoordinates/Simple/{yr_constants.HURRUNGANE_LAT_LON[0]}/{yr_constants.HURRUNGANE_LAT_LON[1]}/1/{before}/{now}'
        ).json()
    except requests.exceptions.HTTPError as err:
        logging.error(
            f'{varsom_constants.API_URL}/AvalancheWarningByCoordinates/Simple/{yr_constants.HURRUNGANE_LAT_LON[0]}/{yr_constants.HURRUNGANE_LAT_LON[1]}/1/{before}/{now} failed: {err}')
        raise SystemExit(err)
