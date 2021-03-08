from rest_framework.fields import IntegerField, SerializerMethodField
from rest_framework.serializers import ModelSerializer

from volleyball.stadium.serializers import StadiumSerializer
from .models import Match

class MatchSerializer(ModelSerializer):

    class Meta:
        model = Match
        stadium = StadiumSerializer()        
        fields = (
            'id', 'stadium', 'home_team', 'away_team', 'match_time', 'base_price'
        )
        read_only_fields = ('id',)
