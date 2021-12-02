from services import api_test
from services import ruterstop_test


if __name__ == '__main__':
    api_test.yr_test()
    if ruterstop_test.init_ruterstop() is True and ruterstop_test.ruterstop_cmd() is True:
        print('ruterstop running')

