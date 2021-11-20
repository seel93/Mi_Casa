import requests

def yr_test():
    r = requests.get('http://192.168.0.17/admin/api.php/stats/summary')
    print(r)

