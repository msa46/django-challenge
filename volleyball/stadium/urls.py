from django.urls import path

from .views import StadiumAPI

urlpatterns = [
    path('', StadiumAPI.as_view(), name='create-list-stadium'),
]