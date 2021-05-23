from rest_framework import serializers


class RequestBodySerializer(serializers.Serializer):
    sensor_1 = serializers.ListField(child=serializers.DecimalField(min_value=0.0, max_digits=20, decimal_places=2))
    sensor_2 = serializers.ListField(child=serializers.DecimalField(min_value=0.0, max_digits=20, decimal_places=2))
    sensor_3 = serializers.ListField(child=serializers.DecimalField(min_value=0.0, max_digits=20, decimal_places=2))
