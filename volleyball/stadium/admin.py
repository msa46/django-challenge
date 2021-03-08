from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Stadium, Seat

admin.site.register(Stadium)
admin.site.register(Seat)