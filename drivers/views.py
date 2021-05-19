from rest_framework import serializers, status
from drivers.serializers import *
from drivers.models import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import *
from rest_framework.views import APIView

class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderSerializer
    # permission_classes = (IsAuthenticated,)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(OrderCreateAPIView, self).dispatch(request, *args, **kwargs)

    def post(self, request, format=None):
        content = {
            'user': request.user.id,
            'lat_start': request.data['lat_start'],
            'long_start': request.data['long_start'],
            'lat_end': request.data['lat_end'],
            'long_end': request.data['long_end'],
            'total_psg': 0,
            'status': 'Waiting',
            'time': request.data['time'],
            'capacity': request.data['capacity'],
            'car_type': request.data['car_type'],
        }
        serializer = OrderSerializer(data=content)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DriverDetailAPIView(ListAPIView):
    # class for get Detail Driver
    # permission_classes = [IsAuthenticated]

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(DriverDetailAPIView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        psg = kwargs['pk']
        queryset = Order.objects.get(pk=psg)
        serializer = DriversListSerializer(queryset)
        return Response(serializer.data)

class RiddingView(APIView):
    #class for change status passenger to Ridding
    # permission_classes = (IsAuthenticated,)
    serializer_class = StatusUpdateSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(RiddingView, self).dispatch(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        order = get_object_or_404(Order, pk=kwargs['id'])
        data = {
            'status': 'Ridding'
        }
        serializer = StatusUpdateSerializer(order, data=data, partial=True)
        if serializer.is_valid():
            order = serializer.save()
            return Response(StatusUpdateSerializer(order).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

