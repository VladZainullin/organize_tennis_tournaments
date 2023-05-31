from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from organizers.models import Organizer


class OrganizerRegistrationForm(UserCreationForm):
    title = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'title', 'password1', 'password2')

    def save(self):
        user = super().save()

        organizer = Organizer(title=self.cleaned_data['title'], user=user)
        organizer.save()

        return user
