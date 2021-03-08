from django.db import transaction
from rest_framework.serializers import Serializer, ListSerializer,IntegerField

from volleyball.match.models import Ticket


class TicketListSerializer(ListSerializer):
    def update(self, instance, validated_data):
        ticket_mapping ={ticket.id: ticket for ticket in instance}
        data_mapping = {item['id']: item for item in validated_data}
        tickets = []
        for ticket_id, data in data_mapping.items():
            ticket = ticket_mapping.get(ticket_id, None)
            if ticket:
                if ticket.state == Ticket.TicketStates.AVAILABLE:
                    tickets.append(self.child.update(ticket, data))
        with transaction.atomic():
            Ticket.objects.bulk_update(tickets)
        return tickets


class TicketSerializer(Serializer):
    id = IntegerField(read_only=True)
    match = IntegerField(required=True)
    seat = IntegerField(required=True)
    price = IntegerField(required=True)
    state = IntegerField(required=True)
    buyer = IntegerField(required=True)

    class Meta:
        list_serializer_class = TicketListSerializer