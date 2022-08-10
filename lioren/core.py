import json
import httpx
from typing import Any, Optional

from lioren.config import LIOREN_BASE_URL as BASE_URL
from lioren.config import LIOREN_TOKEN as TOKEN

RequestParams = dict[str, str]
RequestData = dict[str, Any]
APIResponse = dict[str, Any]


def _get(uri: str, params: Optional[RequestParams]) -> APIResponse:
    response = httpx.get(BASE_URL + uri, headers=__headers(), params=params)
    return response.json()


def _post(
    uri: str, data: Optional[RequestData], params: Optional[RequestParams]
) -> APIResponse:
    response = httpx.post(
        BASE_URL + uri, headers=__headers(), data=json.dumps(data), params=params
    )
    return response.json()


def _put(
    uri: str, data: Optional[RequestData], params: Optional[RequestParams]
) -> APIResponse:
    response = httpx.put(
        BASE_URL + uri, headers=__headers(), data=json.dumps(data), params=params
    )
    return response.json()


def _delete(uri: str, params: Optional[RequestParams]) -> APIResponse:
    response = httpx.delete(BASE_URL + uri, headers=__headers(), params=params)
    return response.json()


def __headers() -> dict[str, str]:
    return {
        "Accept": "application/json",
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
    }
