from django.urls import path
from users import views

urlpatterns = [
    path("users/",views.ListUserAPIView.as_view(),name="User_list"),
    path("users/create/", views.CreateUserAPIView.as_view(),name="User_create"),
    path("users/update/<int:pk>/",views.UpdateUserAPIView.as_view(),name="update_User"),
    path("users/delete/<int:pk>/",views.DeleteUserAPIView.as_view(),name="delete_User")
]