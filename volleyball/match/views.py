from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Match, Ticket
from .serializers import MatchSerializer

class MatchAPI(ListCreateAPIView):

    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticated]
