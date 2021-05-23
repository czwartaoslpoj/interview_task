import pytest


def test_post_endpoint(client, json_payload, successful_json_response):
    endpoint = '/api/v1/standardize'
    res = client.post(endpoint, data=json_payload, format='json')

    assert res.status_code == 200
    assert res.data == successful_json_response


@pytest.mark.parametrize(
    "incorrect_json_payload",
    [
        pytest.param([0.44, 0.22, 0.55, 0.24]),
        pytest.param([0.4456, 0.22, 0.55, 0.24]),
        pytest.param([]),
        pytest.param(["words", "words", "words"])
    ],
    indirect=True,
)
def test_post_endpoint_with_incorrect_data(client, incorrect_json_payload):
    endpoint = '/api/v1/standardize'
    res = client.post(endpoint, data=incorrect_json_payload, format='json')
    assert res.status_code == 400
