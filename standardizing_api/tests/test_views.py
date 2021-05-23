import pytest


def test_post_endpoint(client, json_payload, successful_json_response, endpoint):
    res = client.post(endpoint, data=json_payload, format='json')

    assert res.status_code == 200
    assert res.json() == successful_json_response


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
def test_post_endpoint_with_incorrect_data(client, incorrect_json_payload, endpoint):
    res = client.post(endpoint, data=incorrect_json_payload, format='json')
    assert res.status_code == 400


def test_post_endpoint_with_scaling_exception(mocker, client, json_payload, endpoint):
    mocker.patch('sklearn.preprocessing._data.StandardScaler.fit_transform', side_effect=Exception)

    res = client.post(endpoint, data=json_payload, format='json')

    expected_json = {
        "success": False,
        "error": "Error occurred while transforming data with Scaler."
    }
    assert res.status_code == 400
    assert res.json() == expected_json


def test_post_endpoint_with_parsing_exception(mocker, client, json_payload, endpoint):
    error = "Error occurred while parsing data to response body."
    expected_json = {
        "success": False,
        "error": error
    }

    mocker.patch('standardizing_api.transformer.Transformer.convert_to_list', side_effect=Exception)

    res = client.post(endpoint, data=json_payload, format="json")

    assert res.status_code == 400
    assert res.json() == expected_json


def test_post_endpoint_with_unexpected_error(mocker, client, json_payload, endpoint):
    error = "Unexpected error occurred while standardizing data"
    expected_json = {
        "success": False,
        "error": error
    }
    mocker.patch('standardizing_api.transformer.Transformer.transform', side_effect=Exception)

    res = client.post(endpoint, data=json_payload, format="json")

    assert res.status_code == 400
    assert res.json() == expected_json
