# from django.shortcuts import render
# from rest_framework.generics import ListAPIView
# from rest_framework.generics import CreateAPIView
# from rest_framework.generics import DestroyAPIView
# from rest_framework.generics import UpdateAPIView
# from .serializers import *
# from .models import *
# from rest_framework.permissions import IsAuthenticated

# #View, Create, Update, Delete order table
# class ListorderAPIView(ListAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = order.objects.all()
#     serializer_class = orderSerializer

# class CreateorderAPIView(CreateAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = order.objects.all()
#     serializer_class = orderSerializer

# class UpdateorderAPIView(UpdateAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = order.objects.all()
#     serializer_class = orderSerializer

# class DeleteorderAPIView(DestroyAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = order.objects.all()
#     serializer_class = orderSerializer

# #View, Create, Update, Delete finding_driver table
# class Listfinding_driverAPIView(ListAPIView):
#     """
#     de
#     """
#     permission_classes = (IsAuthenticated,)
#     queryset = finding_driver.objects.all()
#     serializer_class = finding_driverSerializer

# class Createfinding_driverAPIView(CreateAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = finding_driver.objects.all()
#     serializer_class = finding_driverSerializer

# class Updatefinding_driverAPIView(UpdateAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = finding_driver.objects.all()
#     serializer_class = finding_driverSerializer

# class Deletefinding_driverAPIView(DestroyAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = finding_driver.objects.all()
#     serializer_class = finding_driverSerializer

from rest_framework import viewsets
from drivers.serializers import orderSerializer, finding_driverSerializer
from drivers.models import order, finding_driver
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated

class orderViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset =  order.objects.all()
    serializer_class = orderSerializer

class finding_driverViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset =  finding_driver.objects.all()
    serializer_class = finding_driverSerializer