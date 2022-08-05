import json
import httpx
from typing import Optional

from lioren.config import LIOREN_BASE_URL as BASE_URL
from lioren.config import LIOREN_TOKEN as TOKEN


def _get(uri: str, params: Optional[object]):
    response = httpx.get(BASE_URL + uri, headers=__headers(), params=params)
    return response.json()


def _post(uri: str, data: Optional[object], params: Optional[object]):
    response = httpx.post(
        BASE_URL + uri, headers=__headers(), data=json.dumps(data), params=params
    )
    return response.json()


def _put(uri: str, data: Optional[object], params: Optional[object]):
    response = httpx.put(
        BASE_URL + uri, headers=__headers(), data=json.dumps(data), params=params
    )
    return response.json()


def _delete(uri: str, params: Optional[object]):
    response = httpx.delete(BASE_URL + uri, headers=__headers(), params=params)
    return response.json()


def __headers():
    return {
        "Accept": "application/json",
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
    }
