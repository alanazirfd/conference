from .models import Seat
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string, get_template
from django.utils.encoding import force_bytes, force_str    
from email.mime.image import MIMEImage

def getAvaliableSeats():
    return Seat.objects.filter(assigned_to=None).order_by('order').values()

def assignSeat(attendee):
    avaliable_seats_dict = getAvaliableSeats()
    assigned_seat_number = avaliable_seats_dict[0]['seat_number']
    seat = Seat.objects.get(seat_number=assigned_seat_number)
    seat.assigned_to = attendee
    seat.save()
    return seat

def sendConfirmationEmail(attendee):
    mail_subject = "Your registration is successful!"
    message = render_to_string('confirmation.html')

    email_message = EmailMessage(mail_subject, message, to=[attendee.email])
    email_message.content_subtype = "html"

    email_message.send()