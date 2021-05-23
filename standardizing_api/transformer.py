from collections import OrderedDict
from configparser import ParsingError
from typing import Union

import numpy as np
from loguru import logger
from sklearn.preprocessing import StandardScaler

from standardizing_api.models import StandardizeResponseBody, ScalingError, SensorResults


class Transformer():
    def __init__(self):
        self.scaler = StandardScaler()

    def transform(self, validated_data: OrderedDict) -> Union[StandardizeResponseBody, dict]:

        combined_list = []

        try:
            for key, value in validated_data.items():
                combined_list.append(value)

            standardized_data = self.standardize(combined_list)
            response_body = self.parse_results_into_standardize_response_body(standardized_data)

            return response_body

        except ParsingError as e:

            json_response = {
                "success": False,
                "error": e.message
            }
            return json_response

        except ScalingError as e:

            json_response = {
                "success": False,
                "error": e.message
            }
            return json_response

        except Exception as e:

            error_msg = "Unexpected error occurred while standardizing data"
            logger.error(f"{error_msg}: {str(e)}")

            json_response = {
                "success": False,
                "error": error_msg
            }
            return json_response

    def standardize(self, input_list: list) -> np.ndarray:

        try:
            transposed_list = np.array(input_list).T
            transformed_data = self.scaler.fit_transform(transposed_list).T
            logger.success("Data got successfully scaled.")
            return transformed_data

        except Exception as e:
            error_msg = f"Error occurred while scaling data. Exception: {e}"
            logger.error(error_msg)
            raise ScalingError(error_msg)

    def parse_results_into_standardize_response_body(self, results: np.ndarray) -> StandardizeResponseBody:

        try:
            sensor_results = SensorResults(
                self.convert_to_list(results[0]),
                self.convert_to_list(results[1]),
                self.convert_to_list(results[2])
            )
            response_body = StandardizeResponseBody(success=True, result=sensor_results)

            logger.success("Standardized data got successfully parsed into StandardizeResponseBody")

            return response_body

        except Exception as e:
            message = "Error occurred while parsing data to response body."
            logger.error(f"{message} Exception: {e}")
            raise ParsingError(message) from e

    def convert_to_list(self, input_list: np.ndarray) -> list:

        output_list = []

        input_list = input_list.tolist()

        for item in input_list:
            output_list.append(float("{:.8f}".format(item)))
        return output_list
