import logging
import requests
from config import yr_constants


def get_snow_depths_for_region(region_id):
    try:
        return requests.get(
            '{url}/observations/snowdepths/regions/{region_id}'.format(url=yr_constants.YR_API_URL,
                                                                       region_id=region_id),
            headers=yr_constants.YR_HEADERS).json()
    except requests.exceptions.HTTPError as err:
        logging.error(
            '{url}/observations/snowdepths/regions/{region_id} failed: {err}'.format(url=yr_constants.YR_API_URL,
                                                                                     region_id=region_id, err=err))
        raise SystemExit(err)
