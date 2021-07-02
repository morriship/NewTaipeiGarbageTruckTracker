import json
from typing import List

import crawler


class RubbishTruck:

    def __init__(self, line_id: str, car: str, time: str, location: str, longitude: str, latitude: str, city_id: str, city_name: str):
        self.line_id = line_id
        self.car = car
        self.time = time
        self.location = location
        self.longitude = longitude
        self.latitude = latitude
        self.city_id = city_id
        self.city_name = city_name

    def on_street(self, street_name: str) -> bool:
        return street_name in self.location


RubbishTrucks = List[RubbishTruck]


def json_decoder(obj):
    if type(obj) == list:
        result = []
        for child in obj:
            result.append(json_decoder(child))
    else:
        return RubbishTruck(line_id=obj['lineId'],
                            car=obj['car'],
                            time=obj['time'],
                            location=obj['location'],
                            longitude=obj['longitude'],
                            latitude=obj['latitude'],
                            city_id=obj['cityId'],
                            city_name=obj['cityName'])


def get_rubbish_trucks() -> RubbishTrucks:
    json_content = crawler.get_rubbish_trucks_json()
    return json.loads(json_content, object_hook=json_decoder)
