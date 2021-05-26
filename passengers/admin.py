from django.contrib import admin
from .models import *

@admin.register(Passengers)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'order', 'place_pick', 'place_drop', 'fee', )
    list_filter = ('time', 'status', 'order',)
