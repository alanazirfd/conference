from django.shortcuts import render
from .models import Attendee, Seat
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string, get_template
from django.utils.encoding import force_bytes, force_str    
from email.mime.image import MIMEImage

from .functions import getAvaliableSeats, assignSeat, sendConfirmationEmail

from .tokens import account_activation_token

# To open/close registeration
REGISTERATION_OPEN = True

def home(request):
    return render(request, 'main.html')

def register(request):
    
    if request.method == "POST":

        if REGISTERATION_OPEN == False:
            messages.error(request, f"We are sorry, the registeration is currently closed")
            return render(request, 'register.html')

        # Get Attendee data from register form
        name = request.POST.get("name")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        education = request.POST.get("education")
        country = request.POST.get("country")
        phone = request.POST.get("phone")
        email = request.POST.get("email").lower()

        # Check if there is a seat avaliable    
        avaliable_seats_dict = getAvaliableSeats()
        if not avaliable_seats_dict:
            messages.error(request, "Sorry, seats are full")
            return render(request, 'register.html')

        if Attendee.objects.filter(email=email).exists(): # Check if the user is registered
            confirmed = Attendee.objects.filter(email=email).values_list('confirmed', flat=True)[0]
            if confirmed:
                messages.error(request, "The email has already been used")    
                return render(request, 'register.html')
            else:
                Attendee.objects.filter(email=email).delete()
    
        # Create the user
        attendee = Attendee.objects.create(name=name, email=email,
                                            gender=gender, age=age,
                                            education=education, country=country, phone=phone)

        # Send email
        current_site = get_current_site(request)
        mail_subject = 'Confirm your registeration'
        
        message = render_to_string('activate.html', {
            'attendee': attendee,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(attendee.email)),
            'token': account_activation_token.make_token(attendee),
        })
        
        email_message = EmailMessage(mail_subject, message, to=[email])
        email_message.content_subtype = "html"

        if email_message.send():
            messages.success(request, f"A confirmation email has been sent to {email}")
            response = render(request, "register.html")
            response['Location'] = "?status=success" 
            return response
        else:
            messages.error(request, f"An error has happened. Please make sure you entered a correct email")
            render(request, 'register.html')

    return render(request, 'register.html')

def activate(request, uidb64, token):
    attendee = None
    try:
        email_id = force_str(urlsafe_base64_decode(uidb64))
        attendee = Attendee.objects.get(email=email_id)
    except:
        attendee = None
    
    if attendee is not None and account_activation_token.check_token(attendee, token): # Check if token is correct and assign seat
        attendee.confirmed = True
        attendee.save()

        # Assign seat
        seat = assignSeat(attendee)
        sendConfirmationEmail(attendee)
        return render(request, 'register.html')
    else:
        messages.error(request, "An error happened")
        return render(request, 'register.html')
    
def team(request):
    return render(request, 'team.html')

def faculty(request):
    return render(request, 'faculty.html')

def previous_versions(request):
    return render(request, 'previous_versions.html')

def about(request):
    return render(request, 'about.html')

def sponsors(request):
    return render(request, 'sponsors.html')
def scientific_programme(request):
    return render(request, 'scientific_programme.html')





