from django.urls import path
from api import views

urlpatterns = [
    path("users/",views.ListUserAPIView.as_view(),name="User_list"),
    path("users/create/", views.CreateUserAPIView.as_view(),name="User_create"),
    path("users/update/<int:pk>/",views.UpdateUserAPIView.as_view(),name="update_User"),
    path("users/delete/<int:pk>/",views.DeleteUserAPIView.as_view(),name="delete_User"),

    path("order/",views.ListorderAPIView.as_view(),name="order_list"),
    path("order/create/", views.CreateorderAPIView.as_view(),name="order_create"),
    path("order/update/<int:pk>/",views.UpdateorderAPIView.as_view(),name="update_order"),
    path("order/delete/<int:pk>/",views.DeleteorderAPIView.as_view(),name="delete_order"),

    path("finding_driver/",views.Listfinding_driverAPIView.as_view(),name="finding_driver_list"),
    path("finding_driver/create/", views.Createfinding_driverAPIView.as_view(),name="finding_driver_create"),
    path("finding_driver/update/<int:pk>/",views.Updatefinding_driverAPIView.as_view(),name="update_finding_driver"),
    path("finding_driver/delete/<int:pk>/",views.Deletefinding_driverAPIView.as_view(),name="delete_finding_driver"),

    path("request/",views.ListrequestAPIView.as_view(),name="request_list"),
    path("request/create/", views.CreaterequestAPIView.as_view(),name="request_create"),
    path("request/update/<int:pk>/",views.UpdaterequestAPIView.as_view(),name="update_request"),
    path("request/delete/<int:pk>/",views.DeleterequestAPIView.as_view(),name="delete_request"),

    path("transaction/",views.ListtransactionAPIView.as_view(),name="transaction_list"),
    path("transaction/create/", views.CreatetransactionAPIView.as_view(),name="transaction_create"),
    path("transaction/update/<int:pk>/",views.UpdatetransactionAPIView.as_view(),name="update_transaction"),
    path("transaction/delete/<int:pk>/",views.DeletetransactionAPIView.as_view(),name="delete_transaction")
]