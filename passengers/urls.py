from django.urls import path
from passengers.views import *

urlpatterns = [
    path('createpsg/<int:order>/', PassengerCreateAPIView.as_view(), name='passengers_create'),
    path('detail/<int:pk>/', PassengerDetailAPIView.as_view(), name='passengers_detail'),
    path('list/<int:order>/', PassengersListAPIView.as_view(), name='passengers_list'),
    path('pendinglist/<int:order>/', PassengersPendingListAPIView.as_view(), name='passengers_list'),
    path('accepted/<int:id>/', AcceptedView.as_view(), name='passangers_status_accepted'),
    path('denied/<int:id>/', DeniedView.as_view(), name='passangers_status_denied'),
    path('arrived/<int:id>/', ArrivedView.as_view(), name='passangers_status_arrived'),
    path('startride/<int:id>/', StartRideView.as_view(), name='passangers_status_startride'),
    path('completeride/<int:id>/', CompleteRideView.as_view(), name='passangers_status_completeride'),
    path('done/<int:id>/', DoneView.as_view(), name='passangers_status_done'),
]