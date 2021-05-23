from collections import OrderedDict

import numpy as np
import pytest
from rest_framework.test import APIClient

from standardizing_api.transformer import Transformer


@pytest.fixture(scope='module')
def transformer():
    transformer = Transformer()
    return transformer


@pytest.fixture
def validated_data():
    validated_data = (OrderedDict({"sensor_1": [5.44, 3.22, 6.55, 8.54, 1.24],
                                   "sensor_2": [5444.44, 33.22, 622.55, 812.54, 1233.24],
                                   "sensor_3": [0.44, 0.22, 0.55, 0.54, 0.24]}))
    return validated_data


@pytest.fixture
def combined_list():
    combined_list = [[5.44, 3.22, 6.55, 8.54, 1.24],
                     [5444.44, 33.22, 622.55, 812.54, 1233.24],
                     [0.44, 0.22, 0.55, 0.54, 0.24]]
    return combined_list


@pytest.fixture
def transformed_list():
    transformed_list = np.array([[0.17354382, -0.69810162, 0.60936654, 1.39070637, -1.47551512],
                                 [1.96026147, -0.82000937, -0.51721314, -0.41959677, -0.2034422],
                                 [0.29452117, -1.24820879, 1.06588616, 0.99576207, -1.10796061]])
    return transformed_list


@pytest.fixture(scope="session")
def client():
    client = APIClient()
    return client


@pytest.fixture(scope="session")
def json_payload():
    json_payload = {"sensor_1": [5.44, 3.22, 6.55, 8.54, 1.24],
                    "sensor_2": [5444.44, 33.22, 622.55, 812.54, 1233.24],
                    "sensor_3": [0.44, 0.22, 0.55, 0.54, 0.24]}
    return json_payload


@pytest.fixture(scope="session")
def incorrect_json_payload(request):
    incorrect_json_payload = {"sensor_1": request.param,
                              "sensor_2": [5444.44, 33.22, 622.55, 812.54, 1233.24],
                              "sensor_3": [0.44, 0.22, 0.54, 0.24]}
    return incorrect_json_payload

@pytest.fixture(scope="session")
def successful_json_response():
    successful_json_response = {"success": True,
                                "result": {
                                    "sensor1": [0.17354382, -0.69810162, 0.60936654, 1.39070637, -1.47551512],
                                    "sensor2": [1.96026147, -0.82000937, -0.51721314, -0.41959677, -0.2034422],
                                    "sensor3": [0.29452117, -1.24820879, 1.06588616, 0.99576207, -1.10796061]
                                }}
    return successful_json_response

@pytest.fixture(scope="session")
def endpoint():
    endpoint = '/api/v1/standardize'
    return endpoint
