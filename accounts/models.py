from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


class User(AbstractUser):
    phone = models.CharField(_('Phone Number'), max_length=255, blank=True, null=True, unique=True,
                             help_text='Write in international phone no format (+234 or +41)')
    dob = models.DateField(_('Date of Birth'), help_text='Enter birthday in DD-MM-YYYY format ', blank=True, null=True)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    @classmethod
    def get_this_month_birthdays(cls):
        today = datetime.today()
        # get the birthdays
        bday = cls.objects.filter(dob__month=today.month, is_active=True).order_by('dob')
        # give priority to todays bday, order upcoming and reverse order past
        result = list(bday.filter(dob=today)) + list(bday.filter(dob__gt=today).order_by('dob')) + list(
            bday.filter(dob__lt=today).order_by('-dob'))
        return result
