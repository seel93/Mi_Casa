""" Current entrypoint for application """

import logging
import pymongo
from services import api_test
from config import yr_constants, db_credential

logging.basicConfig(level=logging.INFO)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

client = pymongo.MongoClient(db_credential.DB_CONNECTION_STRING)
db = client.test
logging.info(f'connection established on: {db_credential.DB_CONNECTION_STRING}')


if __name__ == '__main__':
    api_test.yr_test_api_health()
    api_test.yr_test_location(yr_constants.SKEI_LAT_LON)
    api_test.yr_multiple_location_test(yr_constants.YR_LOCATION_LIST)
    api_test.yr_location_forecast_test(yr_constants.SKEI_LOCATION_ID)
    api_test.yr_snow_test()
    logging.info('yr tests completed')
    api_test.avalanche_test()
    api_test.get_athlete_test()
    api_test.get_activity_test()
    api_test.get_activities_test()
