from django.db import models
from django.contrib.auth.models import User
from localflavor.in_.models import INStateField
from django.core.validators import RegexValidator

from .utils import user_directory_path


class Location(models.Model):
    address_1 = models.CharField(max_length=128,blank=True)
    address_2 = models.CharField(max_length=128,blank=True)
    city = models.CharField(max_length=64)
    state = INStateField(default="UP")
    zip_code = models.CharField(max_length=6, validators=[RegexValidator(regex=r'^\d{6}$', message="ZIP code must be exactly 6 digits")],blank=True,null=True)

    def __str__(self):
        return f'Location {self.id}'

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path, null=True)
    bio = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(max_length=10, blank=True)
    location = models.OneToOneField(Location,on_delete=models.SET_NULL,null=True)
    # location = models.OneToOneField('users.Location',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'