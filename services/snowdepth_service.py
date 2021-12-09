import logging
import requests
from config import yr_constants
from dao import snow_depth


def get_snow_depths_for_region(region_id):
    try:
        res = requests.get(
            f'{yr_constants.YR_API_URL}/observations/snowdepths/regions/{region_id}',
            headers=yr_constants.YR_HEADERS).json()
        return snow_depth.SnowDepth(
            name=res.get('region').get('name'),
            dates=res.get('dates'),
            stations=res.get('stations')
        )
    except requests.exceptions.HTTPError as err:
        logging.error(
            f'{yr_constants.YR_API_URL}/observations/snowdepths/regions/{region_id} failed: {err}')
        raise SystemExit(err)
