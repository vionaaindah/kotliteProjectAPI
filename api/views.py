from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from api.serializers import UserSerializer
from django.contrib.auth.models import User
from api.serializers import orderSerializer, finding_driverSerializer, requestSerializer, transactionSerializer
from api.models import order, finding_driver, request, transaction
from rest_framework.permissions import IsAuthenticated

# Create your views here.
#View, Create, Update, Delete User table
class ListUserAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateUserAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UpdateUserAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DeleteUserAPIView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

#View, Create, Update, Delete order table
class ListorderAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = order.objects.all()
    serializer_class = orderSerializer

class CreateorderAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = order.objects.all()
    serializer_class = orderSerializer

class UpdateorderAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = order.objects.all()
    serializer_class = orderSerializer

class DeleteorderAPIView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = order.objects.all()
    serializer_class = orderSerializer

#View, Create, Update, Delete finding_driver table
class Listfinding_driverAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = finding_driver.objects.all()
    serializer_class = finding_driverSerializer

class Createfinding_driverAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = finding_driver.objects.all()
    serializer_class = finding_driverSerializer

class Updatefinding_driverAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = finding_driver.objects.all()
    serializer_class = finding_driverSerializer

class Deletefinding_driverAPIView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = finding_driver.objects.all()
    serializer_class = finding_driverSerializer

#View, Create, Update, Delete request table
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

#View, Create, Update, Delete transaction table
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