from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

#url for drivers app
# from drivers import views
# drivers_router = routers.DefaultRouter()
# drivers_router.register(r'order', views.OrderViewSet)
# drivers_router.register(r'findingdriver', views.FindingDriverViewSet)

#url for passengers app
from passengers import views
passengers_router = routers.DefaultRouter()
passengers_router.register(r'request', views.RequestViewSet)
passengers_router.register(r'transaction', views.TransactionViewSet)


urlpatterns = [
    path('admin/', admin.site.urls), #for admin site
    path('docs/', include_docs_urls(title='Kotlite Api')), #for documentation site
    path('users/', include("users.urls")), #for login, refresh token and register site
    path('drivers/', include("drivers.urls")), #for url in drivers app
    path('passengers/', include(passengers_router.urls)), #for url in passengers app
]