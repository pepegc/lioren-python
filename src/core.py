import json
import requests

from lioren.config import LIOREN_BASE_URL as BASE_URL
from lioren.config import LIOREN_TOKEN as TOKEN



def _get(uri, params=None):
    response = requests.get(
        BASE_URL+uri, headers=__headers(), params=params)
    return response.json()


def _post(uri, data=None, params=None):
    response = requests.post(
        BASE_URL+uri, headers=__headers(), data=json.dumps(data), params=params)
    return response.json()



def _put(uri, data=None, params=None):
    response = requests.put(
        BASE_URL+uri, headers=__headers(), data=json.dumps(data), params=params)
    return response.json()


def _delete(uri, params=None):
    response = requests.delete(
        BASE_URL+uri, headers=__headers(), params=params)
    return response.json()


def __headers():
    return {
        'Accept': 'application/json',
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json',
    }
