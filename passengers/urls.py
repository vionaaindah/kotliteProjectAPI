from django.urls import path
from passengers import views

urlpatterns = [
    path("request/",views.ListrequestAPIView.as_view(),name="request_list"),
    path("request/create/", views.CreaterequestAPIView.as_view(),name="request_create"),
    path("request/update/<int:pk>/",views.UpdaterequestAPIView.as_view(),name="update_request"),
    path("request/delete/<int:pk>/",views.DeleterequestAPIView.as_view(),name="delete_request"),

    path("transaction/",views.ListtransactionAPIView.as_view(),name="transaction_list"),
    path("transaction/create/", views.CreatetransactionAPIView.as_view(),name="transaction_create"),
    path("transaction/update/<int:pk>/",views.UpdatetransactionAPIView.as_view(),name="update_transaction"),
    path("transaction/delete/<int:pk>/",views.DeletetransactionAPIView.as_view(),name="delete_transaction")
]