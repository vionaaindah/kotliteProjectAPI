# from django.shortcuts import render
# from rest_framework.generics import ListAPIView
# from rest_framework.generics import CreateAPIView
# from rest_framework.generics import DestroyAPIView
# from rest_framework.generics import UpdateAPIView
# from .serializers import UserSerializer
# from django.contrib.auth.models import User
# from rest_framework.permissions import IsAuthenticated

# # Create your views here.
# #View, Create, Update, Delete User table
# class ListUserAPIView(ListAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class CreateUserAPIView(CreateAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UpdateUserAPIView(UpdateAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class DeleteUserAPIView(DestroyAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

from rest_framework import viewsets
from users.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
#     permission_classes = (IsAuthenticated,)
    queryset =  User.objects.all()
    serializer_class = UserSerializer