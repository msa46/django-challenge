from rest_framework.generics import ListAPIView,UpdateAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_list_or_404, get_object_or_404

from volleyball.match.models import  Ticket
from .serializers import TicketSerializer

class TicketAPI(ListAPIView, UpdateModelMixin):

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]
    
    def get_serializer(self, *args, **kwargs):
        if self.request.method.lower() == 'patch':
            data = kwargs.get('data')
            kwargs['many'] = isinstance(data, list)
        return super(TicketAPI, self).get_serializer(*args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

