import requests


NTPC_URL = 'https://data.ntpc.gov.tw/api/datasets/28AB4122-60E1-4065-98E5-ABCCB69AACA6/json?page=0&size=10000'


def get_rubbish_trucks_json() -> str:
    headers = {'accept': 'application/json'}
    resp = requests.get(NTPC_URL, headers=headers)
    return resp.content
