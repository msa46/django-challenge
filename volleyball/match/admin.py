from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Match, Ticket

admin.site.register(Match)
admin.site.register(Ticket)