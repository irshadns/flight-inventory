from django.contrib import admin
from django.db import models
from .models import User, Airport, Flight

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email')

@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ('iata_code', 'city')


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('origin', 'destination', 'flight_number', 'departure_date_time', 'arrival_date_time', 'base_fare', 'tax')