from django.urls import path
from passengers.views import *

urlpatterns = [
    path('detail/<int:pk>/', PassengerDetailAPIView.as_view(), name='passengers_list'),
    path('list/<int:order>/', PassengersListAPIView.as_view(), name='passengers_list'),
    path('accepted/<int:id>/', AcceptedView.as_view(), name='auth_update_profile'),
    path('denied/<int:id>/', DeniedView.as_view(), name='auth_update_profile'),
    path('arriving/<int:id>/', ArrivingView.as_view(), name='auth_update_profile'),
    path('arrived/<int:id>/', ArrivedView.as_view(), name='auth_update_profile'),
    path('startride/<int:id>/', StartRideView.as_view(), name='auth_update_profile'),
    path('complate/<int:id>/', CompleteRideView.as_view(), name='auth_update_profile'),
    path('done/<int:id>/', DoneView.as_view(), name='auth_update_profile'),
]