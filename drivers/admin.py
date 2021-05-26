from django.contrib import admin
from .models import *

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'place_start', 'place_end', 'income', )
    list_filter = ('time', 'status', )

@admin.register(FindingDriver)
class FindingDriverAdmin(admin.ModelAdmin):
    list_display = ('pk', 'order', 'latitude', 'longitude', 'sequence', )
    list_filter = ('order', )
    
admin.site.site_header = "Kotlite Admin"