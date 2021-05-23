import numpy as np
import pytest

from standardizing_api.models import ScalingError, SensorResults, StandardizeResponseBody, ParsingError


def test_standardize(transformer, combined_list, transformed_list):
    actual_result = transformer.standardize(combined_list)

    assert type(actual_result) == np.ndarray
    assert actual_result.all() == transformed_list.all()


def test_test_standardize_with_exception_raised(mocker, transformer, combined_list):
    mocker.patch('numpy.array', side_effect=Exception)

    with pytest.raises(ScalingError):
        transformer.standardize(combined_list)


def test_convert_to_list(transformer, transformed_list):
    actual_result = transformer.convert_to_list(transformed_list[0])
    expected_len_of_list = 5
    expected_value = 1.39070637

    assert type(actual_result) == list
    assert len(actual_result) == expected_len_of_list
    assert actual_result[3] == expected_value

def test_parse_results_into_standardized_response_body(transformer, transformed_list):

    actual_response_body = transformer.parse_results_into_standardize_response_body(transformed_list)
    sensor1 = [0.17354382, -0.69810162, 0.60936654, 1.39070637, -1.47551512]

    assert type(actual_response_body.result) == SensorResults
    assert type(actual_response_body) == StandardizeResponseBody
    assert actual_response_body.result.sensor1 == sensor1


def test_parse_results_into_standardized_response_body_with_exception(mocker, transformer, transformed_list):

    mocker.patch('standardizing_api.transformer.Transformer.convert_to_list', side_effect = Exception)
    with pytest.raises(ParsingError):
        transformer.parse_results_into_standardize_response_body(transformed_list)


def test_transform(transformer, validated_data):

    sensor1 = [0.17354382, -0.69810162, 0.60936654, 1.39070637, -1.47551512]

    result_body = transformer.transform(validated_data)
    assert type(result_body) == StandardizeResponseBody
    assert result_body.result.sensor1 == sensor1
    assert result_body.success == True
