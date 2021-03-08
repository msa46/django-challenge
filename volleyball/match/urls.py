from django.urls import path
from .views import MatchAPI

urlpatterns = [
    path('', MatchAPI.as_view(), name='create-list-match'),
]
