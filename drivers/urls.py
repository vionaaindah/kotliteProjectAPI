from django.urls import path
from drivers.views import *

urlpatterns = [
    path('createorder/', OrderCreateAPIView.as_view(), name='drivers_createorder'),
    path('detail/<int:pk>/', DriverDetailAPIView.as_view(), name='drivers_createorder'),
    path('ridding/<int:id>/', RiddingView.as_view(), name='auth_update_profile'),
]