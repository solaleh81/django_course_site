from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    meetups = [
        {'Meetup 1'},
        {'Meetup 2'}
    ]
    return render(request, 'meetups/index.html', context={'meetups': meetups})
