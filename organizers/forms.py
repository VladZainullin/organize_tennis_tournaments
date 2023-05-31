from django.contrib.auth.forms import UserCreationForm
from django import forms

from organizers.models import Organizer


class OrganizerRegistrationForm(UserCreationForm):
    title = forms.CharField(max_length=50)

    class Meta:
        model = Organizer
        fields = ('username', 'password1', 'password2')
