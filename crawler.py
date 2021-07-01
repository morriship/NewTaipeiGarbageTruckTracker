import json

import requests

import rubbish_truck


NTPC_URL = 'https://data.ntpc.gov.tw/api/datasets/28AB4122-60E1-4065-98E5-ABCCB69AACA6/json?page=0&size=10000'


def get_rubbish_trucks() -> rubbish_truck.RubbishTrucks:
    headers = {'accept': 'application/json'}
    resp = requests.get(NTPC_URL, headers=headers)
    rubbish_trucks = json.loads(resp.content, object_hook=rubbish_truck.json_decoder)
    return rubbish_trucks
