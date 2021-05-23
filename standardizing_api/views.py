import json

from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.request import Request

from standardizing_api.serializers import RequestBodySerializer

class StandardizerView(viewsets.ViewSet):

    def supervise_standardization(self, request: Request):

        serializer = RequestBodySerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            print(validated_data)
            return HttpResponse({'data':'is_there'})

standardizer_view = StandardizerView.as_view({"post": "supervise_standardization"})
