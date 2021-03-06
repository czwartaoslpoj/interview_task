import json

from django.http import HttpResponse
from loguru import logger
from rest_framework import viewsets
from rest_framework.request import Request

from standardizing_api.models import ParsingError, ScalingError
from standardizing_api.serializers import RequestBodySerializer
from standardizing_api.transformer import Transformer


class StandardizerView(viewsets.ViewSet):
    transformer = Transformer()

    def supervise_standardization(self, request: Request) -> HttpResponse:
        """
        Preform standardization on data retrieved from request.
        1. Check if data retrieved from request is valid with help of Serializer
        2. Transform validated data with Transformer class
        3. Return HttpResponse standardized data or error message
        """

        serializer = RequestBodySerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            try:
                transformed_data = self.transformer.transform(validated_data)
                logger.success("Data got successfully standardized.")
                return HttpResponse(json.dumps(transformed_data.as_dict()), content_type="application/json")

            except (ParsingError, ScalingError) as e:

                json_response = {
                    "success": False,
                    "error": e.message
                }
                return HttpResponse(json.dumps(json_response),
                                    content_type="application/json",
                                    status=400)

            except Exception as e:

                error_msg = "Unexpected error occurred while standardizing data"
                logger.error(f"{error_msg}: {str(e)}")

                json_response = {
                    "success": False,
                    "error": error_msg
                }
                return HttpResponse(json.dumps(json_response),
                                    content_type="application/json",
                                    status=400)
        else:
            return HttpResponse(serializer.errors, status=400)


standardizer_view = StandardizerView.as_view({"post": "supervise_standardization"})
