from rest_framework.serializers import ModelSerializer

from .models import Stadium

class StadiumSerializer(ModelSerializer):


    class Meta:
        model = Stadium
        fields = (
            'id', 'name', 'row', 'seats_in_row'
        )

        read_only_fields = ('id',) #As ID Should not be writable