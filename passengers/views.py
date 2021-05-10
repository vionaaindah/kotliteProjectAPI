from rest_framework import viewsets
from passengers.serializers import *
from passengers.models import *
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated

class RequestViewSet(viewsets.ModelViewSet):
#     permission_classes = (IsAuthenticated,)
    queryset =  Request.objects.all()
    serializer_class = RequestSerializer

class TransactionViewSet(viewsets.ModelViewSet):
#     permission_classes = (IsAuthenticated,)
    queryset =  Transaction.objects.all()
    serializer_class = TransactionSerializer