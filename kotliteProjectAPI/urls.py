from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls), #for admin site
    path('docs/', include_docs_urls(title='Kotlite Api')), #for documentation site
    path('users/', include("users.urls")), #for login, refresh token and register site
    path('drivers/', include("drivers.urls")), #for url in drivers app
    path('passengers/', include("passengers.urls")), #for url in passengers app
]