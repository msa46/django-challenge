from django.urls import path
from .views import TicketAPI

urlpatterns = [
    path('<int:pk>', TicketAPI.as_view(), name='update-list-Ticket'),
]
