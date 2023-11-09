from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup

def index(request):
    meetups = Meetup.objects.all()
    return render(
        request,
        "meetups/index.html",
        context={"show_meetups": True, "meetups": meetups},
    )


def meetup_details(request, meetup_slug):
    selected_meetup = {
        "title": "A First Meetup",
        "description": "This is the first meetup!",
    }
    return render(
        request,
        "meetups/meetup-details.html",
        context={
            "meetup_title": selected_meetup["title"],
            "meetup_description": selected_meetup["description"],
        },
    )
