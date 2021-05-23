import json

from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.request import Request

from standardizing_api.serializers import RequestBodySerializer
from standardizing_api.transformer import Transformer


class StandardizerView(viewsets.ViewSet):
    transformer = Transformer()

    def supervise_standardization(self, request: Request):

        serializer = RequestBodySerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            transformed_data = self.transformer.transform(validated_data)
            return HttpResponse(json.dumps(transformed_data.as_dict()), content_type="application/json")
        else:
            return HttpResponse(serializer.errors, status=400)


standardizer_view = StandardizerView.as_view({"post": "supervise_standardization"})
