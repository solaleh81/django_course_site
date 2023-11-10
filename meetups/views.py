from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Meetup, Participant
from .forms import RegistrationForm

def index(request):
    meetups = Meetup.objects.all()
    return render(
        request,
        "meetups/index.html",
        context={"show_meetups": True, "meetups": meetups},
    )



def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration')


        return render(request, 'meetups/meetup-details.html', {
                'meetup_found': True,
                'selected_meetup': selected_meetup,
                'form': registration_form
            })
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        })


def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-success.html', context={
        'organizer_email': meetup.organizer_email,
    })