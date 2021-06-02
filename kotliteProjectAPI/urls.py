from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls, api_settings

urlpatterns = [
    path('kotliteadm/', admin.site.urls),  # for admin site
    path('docs/', include_docs_urls(title='Kotlite Api',
                                    schema_url='https://yourapi.com/')),  # for documentation site
    # for login, refresh token and register site
    path('users/', include("users.urls")),
    path('drivers/', include("drivers.urls")),  # for url in drivers app
    # for url in passengers app
    path('passengers/', include("passengers.urls")),
]
