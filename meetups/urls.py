from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path("meetups/", views.index, name="all-meetups"),
    path('meetups/<slug:meetup_slug>/success', views.confirm_registration, name="confirm-registration"),
    path("meetups/<slug:meetup_slug>", views.meetup_details, name="meetup-detail"),
]
