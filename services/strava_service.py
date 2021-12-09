import requests
from config import strava_constants
import logging


def get_athlete():
    try:
        res = requests.get(f'{strava_constants.STRAVA_URL}/athlete',
                           params={'access_token': strava_constants.STRAVA_ACCESS_TOKEN})
        print(res.json())
    except requests.exceptions.HTTPError as err:
        logging.error(f'{strava_constants.STRAVA_URL}/athlete failed: {err}')
        raise SystemExit(err)


def get_activity(activity_id):
    try:
        return requests.get(
            f'{strava_constants.STRAVA_URL}/activities/{6312456143}',
            params={'access_token': strava_constants.STRAVA_ACCESS_TOKEN}
        ).json()
    except requests.exceptions.HTTPError as err:
        logging.error(
            f'{strava_constants.STRAVA_URL}/activities/{6312456143} failed: {err}')
        raise SystemExit(err)


def get_activities():
    try:
        res = requests.get(f'{strava_constants.STRAVA_URL}/athlete/activities',
                           params={'access_token': strava_constants.STRAVA_ACCESS_TOKEN})
        res.raise_for_status()
        print(res.json())
    except requests.exceptions.HTTPError as err:
        logging.error(f'{strava_constants.STRAVA_URL}/athlete/activities failed: {err}')
        raise SystemExit(err)
