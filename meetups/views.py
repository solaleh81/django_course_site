from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    meetups = [
        {'title': 'Meetup 1', 'location': 'New york', 'slug': 'a first meetup'},
        {'title':'Meetup 2', 'location': 'Paris', 'slug': 'a second meetup'},
    ]
    return render(request, 'meetups/index.html', context={'show_meetups': True, 'meetups': meetups})
