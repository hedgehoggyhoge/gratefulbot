import requests


def update_number_of_users():
    r = requests.get('http://cm02240.tmweb.ru/update')
    if r.status_code != 200:
        print('metrics are broken')