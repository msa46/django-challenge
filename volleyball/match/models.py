from django.db import models
from django.contrib.auth.models import User
from volleyball.stadium.models import Stadium, Seat


class Match(models.Model):
    """The idea behind base price is as something that would be used now 
    for the tickets but maybe changed late(used with multipliers,etc.)"""
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    home_team = models.CharField(blank=False, null= False, max_length=50)
    away_team = models.CharField(blank=False, null=False, max_length=50)
    match_time = models.DateTimeField(blank=False, null=False)
    base_price = models.PositiveIntegerField(blank=False, null=False)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        tickets = []
        seats = Seat.objects.filter(stadium=self.stadium)
        for seat in seats:
            tickets.append(Ticket(match=self, seat=seat, price=self.base_price))
        Ticket.objects.bulk_create(tickets)
        #As a final note,I wanted to add a celery task  for expiring all 
        #tickets of a match but alas,Never got the time to do so

class Ticket(models.Model):

    class TicketStates(models.IntegerChoices):
        AVAILABLE = 1
        SOLD = 2
        OUTOFORDER = 3
        EXPIRED = 4
    
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name= "ticketmatch")
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name="ticketseat")
    price =  models.PositiveIntegerField(blank=False, null=False)
    state = models.PositiveIntegerField(choices=TicketStates.choices, default=TicketStates.AVAILABLE)
    buyer = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
