from dataclasses import dataclass


@dataclass
class SensorResults:
    sensor1: list
    sensor2: list
    sensor3: list


@dataclass
class StandardizeResponseBody:
    success: bool
    result: SensorResults


class ParsingError(Exception):
    def __init__(self, message):
        self.message = message

class ScalingError(Exception):
    def __init__(self, message):
        self.message = message
