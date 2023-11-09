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
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        return render(
            request,
            "meetups/meetup-details.html",
            context={
                "meetup_found": True,
                "meetup_title": selected_meetup.title,
                "meetup_description": selected_meetup.description,
                "selected_meetup": selected_meetup,
            },
        )
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', context={"meetup_found": False})