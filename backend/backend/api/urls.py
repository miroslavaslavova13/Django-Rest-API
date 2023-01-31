from django.urls import path

from backend.api.views import api_home

urlpatterns = [
    path('', api_home)
]