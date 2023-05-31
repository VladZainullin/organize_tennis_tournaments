from django.shortcuts import render
from organizers.forms import OrganizerRegistrationForm


def register_organizer(request):
    if request.method == 'POST':
        form = OrganizerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OrganizerRegistrationForm()

    return render(request, 'registration.html', {'form': form})
