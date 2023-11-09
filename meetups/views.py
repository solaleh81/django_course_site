from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    meetups = [
        {"title": "Meetup 1", "location": "New york", "slug": "a first meetup"},
        {"title": "Meetup 2", "location": "Paris", "slug": "a second meetup"},
    ]
    return render(
        request,
        "meetups/index.html",
        context={"show_meetups": True, "meetups": meetups},
    )


def meetup_details(request):
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
