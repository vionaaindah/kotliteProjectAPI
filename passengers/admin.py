from django.contrib import admin
from .models import *

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'order', 'lat_pick', 'long_pick', 'lat_drop', 'long_drop', )
    list_filter = ('time', 'status', )

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'request', 'fee', )
    list_filter = ('status', )
