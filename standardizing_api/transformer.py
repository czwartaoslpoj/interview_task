from collections import OrderedDict

import numpy as np
from sklearn.preprocessing import StandardScaler

class Transformer():
    def __init__(self):
        self.scaler = StandardScaler()

    def transform(self, validated_data: OrderedDict):

        list_with_all_data = []


        for key, value in validated_data.items():
            list_with_all_data.append(value)
        transformed_data = self.standardize(list_with_all_data)
        return transformed_data



    def standardize(self, input_list: list) -> np.ndarray:


        transposed_list = np.array(input_list).T
        transformed_data = self.scaler.fit_transform(transposed_list).T

        return transformed_data
