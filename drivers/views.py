from drivers.serializers import *
from drivers.models import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import *

class OrderCreateAPIView(CreateAPIView):
    """
    Create a new Order entry with Finding_Driver entry
    """
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    # permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = OrderCreateSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ListOrderAPIView(ListAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, pk, *args, **kwargs):
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

class ListFindingDriverAPIView(ListAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = FindingDriver.objects.all()
    serializer_class = FindingDriverSerializer
