from services import api_test
from services import yr_constants


if __name__ == '__main__':
    api_test.yr_test_api_health()
    api_test.yr_test_location(yr_constants.SKEI_LAT_LON)
    api_test.yr_multiple_location_test(yr_constants.YR_LOCATION_LIST)

