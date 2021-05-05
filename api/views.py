from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from api.serializers import UserSerializer
from django.contrib.auth.models import User
from api.serializers import orderSerializer, finding_driverSerializer, requestSerializer, transactionSerializer
from api.models import order, finding_driver, request, transaction

# Create your views here.
#User
class ListUserAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateUserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UpdateUserAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DeleteUserAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#order
class ListorderAPIView(ListAPIView):
    queryset = order.objects.all()
    serializer_class = orderSerializer

class CreateorderAPIView(CreateAPIView):
    queryset = order.objects.all()
    serializer_class = orderSerializer

class UpdateorderAPIView(UpdateAPIView):
    queryset = order.objects.all()
    serializer_class = orderSerializer

class DeleteorderAPIView(DestroyAPIView):
    queryset = order.objects.all()
    serializer_class = orderSerializer

#finding_driver
class Listfinding_driverAPIView(ListAPIView):
    queryset = finding_driver.objects.all()
    serializer_class = finding_driverSerializer

class Createfinding_driverAPIView(CreateAPIView):
    queryset = finding_driver.objects.all()
    serializer_class = finding_driverSerializer

class Updatefinding_driverAPIView(UpdateAPIView):
    queryset = finding_driver.objects.all()
    serializer_class = finding_driverSerializer

class Deletefinding_driverAPIView(DestroyAPIView):
    queryset = finding_driver.objects.all()
    serializer_class = finding_driverSerializer

#request
class ListrequestAPIView(ListAPIView):
    queryset = request.objects.all()
    serializer_class = requestSerializer

class CreaterequestAPIView(CreateAPIView):
    queryset = request.objects.all()
    serializer_class = requestSerializer

class UpdaterequestAPIView(UpdateAPIView):
    queryset = request.objects.all()
    serializer_class = requestSerializer

class DeleterequestAPIView(DestroyAPIView):
    queryset = request.objects.all()
    serializer_class = requestSerializer

#transaction
class ListtransactionAPIView(ListAPIView):
    queryset = transaction.objects.all()
    serializer_class = transactionSerializer

class CreatetransactionAPIView(CreateAPIView):
    queryset = transaction.objects.all()
    serializer_class = transactionSerializer

class UpdatetransactionAPIView(UpdateAPIView):
    queryset = transaction.objects.all()
    serializer_class = transactionSerializer

class DeletetransactionAPIView(DestroyAPIView):
    queryset = transaction.objects.all()
    serializer_class = transactionSerializer