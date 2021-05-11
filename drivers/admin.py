from django.contrib import admin
from .models import *

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'lat_start', 'long_start', 'lat_end', 'long_end', )
    list_filter = ('time', 'status', )

@admin.register(FindingDriver)
class FindingDriverAdmin(admin.ModelAdmin):
    list_display = ('pk', 'order', 'lat_start_point', 'long_start_point', 'lat_end_point', 'long_end_point', )
    list_filter = ('time', )
    
admin.site.site_header = "Kotlite Admin"