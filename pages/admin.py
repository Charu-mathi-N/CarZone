from .models import Team
from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def Photo(Self, object):
        return format_html('<img src="{}" width="40" style= "border-radius: 50px;"/>'.format(object.photo.url))

    list_display = ('id', 'Photo', 'first_name', 'designation', 'created_date')
    list_display_links = ("id","Photo", "first_name")
    search_fields = ("first_name", "designation")
    list_filter = ('designation',)
admin.site.register(Team, TeamAdmin)
