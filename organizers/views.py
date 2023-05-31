from django.shortcuts import render

from organizers.forms import OrganizerRegistrationForm


def register_organizer(request):
    if request.method != 'POST':
        pass

    form = OrganizerRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'home.html')

    return render(
        request,
        'authentication/registration/registration-organizer.html',
        {'form': form})
