from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    meetups = [
        {'title': 'Meetup 1'},
        {'title':'Meetup 2'},
    ]
    return render(request, 'meetups/index.html', context={'show_meetups': True, 'meetups': meetups})
