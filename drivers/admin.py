from django.contrib import admin
from .models import *

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'lat_start', 'long_start', 'lat_end', 'long_end', )
    list_filter = ('time', 'status', )

@admin.register(FindingDriver)
class FindingDriverAdmin(admin.ModelAdmin):
    list_display = ('pk', 'order', 'latitude', 'longitude', )
    list_filter = ('order', )
    
admin.site.site_header = "Kotlite Admin"