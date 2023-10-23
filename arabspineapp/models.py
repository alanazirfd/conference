from django.db import models

GENDER_CHOICES = (
    ('male', 'male'),
    ('female', 'female'),
)

EDUCATION_CHOICES = (
    ('physician', 'physician'),
    ('nurse', 'nurse'),
    ('physician assistant', 'physician assistant'),
    ('pharmacist', 'pharmacist'),
    ('PhD', 'PhD'),
    ('student', 'student'),
    ('other', 'other'),
)

COUNTRY_CHOICES = (
    ('saudi', 'saudi'),
    ('kuwait', 'kuwait'),
    ('egypt', 'egypt'),
    ('other', 'other'),
)

# Create your models here.
class Attendee(models.Model):
    name = models.CharField(max_length=50, blank=False)
    gender = models.CharField(
        max_length=50,
        choices=GENDER_CHOICES,
    )

    education = models.CharField(
        max_length=50,
        choices=EDUCATION_CHOICES,
    )

    phone = models.IntegerField()
    email = models.EmailField(blank=False)

    # Tracks if attendee confirmed registration using their email
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email

class Seat(models.Model):
    order = models.AutoField(primary_key=True)
    assigned_to = models.OneToOneField(
        Attendee,
        on_delete=models.SET_NULL,
        null=True
    )
    seat_number = models.CharField(max_length=5)

    def __str__(self):
        return self.seat_number