from rest_framework import serializers


class RequestBodySerializer(serializers.Serializer):
    sensor_1 = serializers.ListField(child=serializers.DecimalField(min_value=0.0, max_digits=20, decimal_places=2))
    sensor_2 = serializers.ListField(child=serializers.DecimalField(min_value=0.0, max_digits=20, decimal_places=2))
    sensor_3 = serializers.ListField(child=serializers.DecimalField(min_value=0.0, max_digits=20, decimal_places=2))

    def validate(self, data):
        """ In order for data to be standardized, all lists need to be of the same size """

        if len(data["sensor_1"]) == len(data["sensor_2"]) == len(data["sensor_3"]):
            return data
        else:
            raise serializers.ValidationError("Input lists are not of equal size")
    class Meta:
        fields = ['sensor_1', 'sensor_2', 'sensor_3']
