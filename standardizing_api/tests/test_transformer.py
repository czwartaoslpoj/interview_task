import numpy as np
import pytest

from standardizing_api.models import ScalingError


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
