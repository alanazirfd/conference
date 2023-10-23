from django.apps import AppConfig
from django.db.models.signals import post_migrate

SEAT_COUNT = 100

class TedxappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'arabspineapp'
    
    def ready(self):

        # Only import after the app is ready
        global Seat
        from .models import Seat

        # Create all seats after migration
        post_migrate.connect(createSeats ,sender=self)

def createSeats(sender, **kwargs): # A function that creates all the seats
    # List of all seats
    seat_numbers = [s for s in range(1, SEAT_COUNT+1)]
    for seat_number in seat_numbers:
        if not Seat.objects.filter(seat_number=seat_number).exists():
            Seat.objects.create(seat_number=seat_number)


