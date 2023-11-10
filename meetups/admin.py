from django.contrib import admin
from .models import Meetup

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')


admin.site.register(Meetup, MeetupAdmin)