from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated

# Create your views here.
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