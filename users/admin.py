from django.contrib import admin
from .models import *

@admin.register(Profile)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'phone',)
