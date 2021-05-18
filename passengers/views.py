from rest_framework import viewsets
from passengers.serializers import *
from passengers.models import *
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated

class PassengersViewSet(viewsets.ModelViewSet):
#     permission_classes = (IsAuthenticated,)
    queryset =  Passengers.objects.all()
    serializer_class = PassengersSerializer
