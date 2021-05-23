from dataclasses import dataclass


@dataclass
class SensorResults:
    sensor1: list
    sensor2: list
    sensor3: list

    def as_dict(self):
        return {'sensor1': self.sensor1, 'sensor2': self.sensor2, 'sensor3': self.sensor3}


@dataclass
class StandardizeResponseBody:
    success: bool
    result: SensorResults

    def as_dict(self):
        return {'success': self.success, 'result': self.result.as_dict()}


class ParsingError(Exception):
    def __init__(self, message):
        self.message = message


class ScalingError(Exception):
    def __init__(self, message):
        self.message = message
