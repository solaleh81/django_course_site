from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup
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
        registration_form = RegistrationForm()
        return render(
            request,
            "meetups/meetup-details.html",
            context={
                "meetup_found": True,
                "selected_meetup": selected_meetup,
                'form': registration_form,form to
            },
        )
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', context={"meetup_found": False})