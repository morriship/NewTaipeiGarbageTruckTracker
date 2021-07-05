from abc import ABC, abstractmethod

import requests


NTPC_URL = 'https://data.ntpc.gov.tw/api/datasets/28AB4122-60E1-4065-98E5-ABCCB69AACA6/{content_type}?page=0&size=10000'


class ContentType(ABC):

    @classmethod
    @abstractmethod
    def get_header(cls) -> str:
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def get_url_subpath(cls) -> str:
        raise NotImplementedError()


class ContentJSON(ContentType):

    @classmethod
    def get_header(cls) -> str:
        return 'application/json'

    @classmethod
    def get_url_subpath(cls) -> str:
        return 'json'


def get_rubbish_trucks(ct: ContentType) -> str:
    headers = {'accept': ct.get_header()}
    url = NTPC_URL.format(content_type=ct.get_url_subpath())
    resp = requests.get(url, headers=headers)
    return resp.content
