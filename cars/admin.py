from cars.models import Car
from django.contrib import admin
from .models import Car
from django.utils.html import format_html

class CarAdmin(admin.ModelAdmin):
    def Photo(Self, object):
        return format_html('<img src="{}" width="50" style= "border-radius: 50px;"/>'.format(object.car_photo_1.url))

    list_display = ('car_title', 'Photo', 'model', 'color', 'city', 'year', 'body_style', 'is_featured')
    list_display_links = ("car_title", "Photo", "model")
    list_editable = ('is_featured',)
    search_fields = ("car_title", "city", 'model', 'color')
    list_filter = ("city", 'model', 'color')
    
# Register your models here.
admin.site.register(Car, CarAdmin)