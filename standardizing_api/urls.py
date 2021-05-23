from django.urls import path

from standardizing_api.views import (
    standardizer_view
)

app_name = "standardize"
urlpatterns = [
    path("standardize", view=standardizer_view,  name="standardize")
]
