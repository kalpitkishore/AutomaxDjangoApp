from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from .models import Location, Profile
from .widgets import CustomPictureImageFieldWidget


class UserForm(forms.ModelForm):
    username = forms.CharField(disabled=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

class ProfileForm(forms.ModelForm):
    photo = forms.ImageField(widget=CustomPictureImageFieldWidget)
    bio = forms.TextInput()

    class Meta:
        model = Profile
        fields = ('photo', 'bio', 'phone_number') 

class LocationForm(forms.ModelForm):
    address_1 = forms.CharField(required=True)
    zip_code = forms.CharField(validators=[RegexValidator(regex=r'^\d{6}$', message="ZIP code must be exactly 6 digits")],required=True)
    class Meta:
        model = Location
        fields = ('address_1', 'address_2', 'city', 'state', 'zip_code')