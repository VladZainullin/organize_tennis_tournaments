from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm

from organizers.models import Organizer


class OrganizerRegistrationForm(UserCreationForm):
    title = forms.CharField(max_length=100)

    class Meta:
        model = Organizer
        fields = ('username', 'title', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.title = self.cleaned_data['title']

        if commit:
            user.save()

        return user
