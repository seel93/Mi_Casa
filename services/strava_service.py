import requests
from config import strava_constants
import logging


def get_athlete():
    try:
        res = requests.get('{url}/athlete'.format(url=strava_constants.STRAVA_URL),
                           params={'access_token': strava_constants.STRAVA_ACCESS_TOKEN})
        print(res.json())
    except requests.exceptions.HTTPError as err:
        logging.error('{url}/athlete failed: {err}'.format(url=strava_constants.STRAVA_URL, err=err))
        raise SystemExit(err)


def get_activity(activity_id):
    try:
        return requests.get(
            '{url}/activities/{id}'.format(url=strava_constants.STRAVA_URL, id=6312456143),
            params={'access_token': strava_constants.STRAVA_ACCESS_TOKEN}
        ).json()
    except requests.exceptions.HTTPError as err:
        logging.error(
            '{url}/activities/{id} failed: {err}'.format(url=strava_constants.STRAVA_URL, id=6312456143, err=err))
        raise SystemExit(err)


def get_activities():
    try:
        res = requests.get('{url}/athlete/activities'.format(url=strava_constants.STRAVA_URL),
                           params={'access_token': strava_constants.STRAVA_ACCESS_TOKEN})
        res.raise_for_status()
        print(res.json())
    except requests.exceptions.HTTPError as err:
        logging.error('{url}/athlete/activities failed: {err}'.format(url=strava_constants.STRAVA_URL, err=err))
        raise SystemExit(err)
