from django.contrib import admin

# Register your models here.

from .models import Attendee, Seat

class SeatAdmin(admin.ModelAdmin):
    readonly_fields = ('order', 'assigned_to', 'seat_number')

admin.site.register(Attendee)
admin.site.register(Seat, SeatAdmin)