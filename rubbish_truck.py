import json
from datetime import datetime
from typing import List

import fetcher


TIME_FORMAT = '%Y/%m/%d %H:%M:%S'


class RubbishTruck:

    def __init__(self, line_id: str, car: str, updated_at: datetime, location: str, longitude: str, latitude: str, city_id: str, city_name: str):
        self.line_id = line_id
        self.car = car
        self.updated_at = updated_at
        self.location = location
        self.longitude = longitude
        self.latitude = latitude
        self.city_id = city_id
        self.city_name = city_name

    def __str__(self):
        return '{date}\t{location}'.format(
            date=datetime.strftime(self.updated_at, TIME_FORMAT),
            location=self.location
        )

    def on_street(self, street_name: str) -> bool:
        return street_name in self.location


RubbishTrucks = List[RubbishTruck]


def __parse_datetime(dt: str):
    return datetime.strptime(dt, TIME_FORMAT)


def json_decoder(obj):
    if type(obj) == list:
        result = []
        for child in obj:
            result.append(json_decoder(child))
    else:
        updated_at = __parse_datetime(obj['time'])
        return RubbishTruck(line_id=obj['lineId'],
                            car=obj['car'],
                            updated_at=updated_at,
                            location=obj['location'],
                            longitude=obj['longitude'],
                            latitude=obj['latitude'],
                            city_id=obj['cityId'],
                            city_name=obj['cityName'])


def get_rubbish_trucks() -> RubbishTrucks:
    json_content = fetcher.get_rubbish_trucks(fetcher.ContentJSON)
    return json.loads(json_content, object_hook=json_decoder)
