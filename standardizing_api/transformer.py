from collections import OrderedDict


import numpy as np
from loguru import logger
from sklearn.preprocessing import StandardScaler

from standardizing_api.models import StandardizedResponseBody, ScalingError, SensorResults, ParsingError


class Transformer():
    def __init__(self):
        self.scaler = StandardScaler()

    def transform(self, validated_data: OrderedDict) -> StandardizedResponseBody:
        """
        Transform data validated by Serializer.
        1.Create list containing list with decimal values of sensors
        2.Use StandardScaler in order to standardize data
        3.Parse transformed data into StandardizeResponseBody
        """

        combined_list = []

        for key, value in validated_data.items():
            combined_list.append(value)

        standardized_data = self.standardize(combined_list)
        standardized_response_body = self.parse_results_into_standardized_response_body(standardized_data)

        return standardized_response_body

    def standardize(self, input_list: list) -> np.ndarray:
        """
        Take list with lists of decimal values, transpose it and transform.
        Returns transformed data in type of numpy array.
        In case of any Exceptions encountered raise ScalingError
        """

        try:
            transposed_list = np.array(input_list).T
            transformed_data = self.scaler.fit_transform(transposed_list).T
            logger.success("Data got successfully scaled.")
            return transformed_data

        except Exception as e:
            error_msg = "Error occurred while transforming data with Scaler."
            logger.error(f"{error_msg}. Exception:{e}")
            raise ScalingError(error_msg) from e

    def parse_results_into_standardized_response_body(self, results: np.ndarray) -> StandardizedResponseBody:
        """
        Parse result of transformation to StandardizedResponseBudy dataclass.
        n case of exception encountered raise ParsingError.

        """
        try:
            sensor_results = SensorResults(
                self.convert_to_list(results[0]),
                self.convert_to_list(results[1]),
                self.convert_to_list(results[2])
            )
            response_body = StandardizedResponseBody(success=True, result=sensor_results)

            logger.success("Standardized data got successfully parsed into StandardizeResponseBody")

            return response_body

        except Exception as e:
            message = "Error occurred while parsing data to response body."
            logger.error(f"{message} Exception: {e}")
            raise ParsingError(message) from e

    def convert_to_list(self, input_list: np.ndarray) -> list:
        """
        Convert numpy array to list. Trim decimals.
        """

        output_list = []
        input_list = input_list.tolist()

        for item in input_list:
            output_list.append(float("{:.8f}".format(item)))
        return output_list
