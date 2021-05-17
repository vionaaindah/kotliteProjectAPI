from django.urls import path
from drivers.views import *

urlpatterns = [
    path('createorder/', OrderCreateAPIView.as_view(), name='drivers_createorder'),
    path('order/', ListOrderAPIView.as_view(), name='drivers_createorder'),
    path('order/<int:pk>/', OrderAPIView.as_view(), name='drivers_createorder'),
    path('findingdriver/', ListFindingDriverAPIView.as_view(), name='drivers_createorder'),
]