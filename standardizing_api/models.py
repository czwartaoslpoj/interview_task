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

