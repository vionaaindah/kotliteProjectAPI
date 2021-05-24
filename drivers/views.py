from rest_framework import serializers, status
from drivers.serializers import *
from drivers.models import *
from passengers.models import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import *
from rest_framework.views import APIView
import requests

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
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        API_KEY = 'AIzaSyC9rKUqSrytIsC7QrPExD8v7oLNB3eOr5k'
        LAT_START = request.data['lat_start']
        LONG_START = request.data['long_start']
        LAT_END = request.data['lat_end']
        LONG_END = request.data['long_end']
        
        response = requests.get(f'https://maps.googleapis.com/maps/api/directions/json?origin={LAT_START},{LONG_START}&destination={LAT_END},{LONG_END}&key={API_KEY}')
        data = response.json()
        routes = data['routes'][0]['legs'][0]['steps']
        
        LAT_ROUTES = [] 
        LONG_ROUTES = []
        
        for route in routes:
            lat_start = route['start_location']['lat']
            long_start = route['start_location']['lng']
            lat_end = route['end_location']['lat']
            long_end = route['end_location']['lng']
                
            if lat_start not in LAT_ROUTES:
                LAT_ROUTES.append(lat_start)
            if long_start not in LONG_ROUTES:
                LONG_ROUTES.append(long_start)
            if lat_end not in LAT_ROUTES:
                LAT_ROUTES.append(lat_end)
            if long_end not in LONG_ROUTES:
                LONG_ROUTES.append(long_end)
                            
        id=request.user.pk
        queryset = Order.objects.filter(user=id).last()
        for i in range(len(LAT_ROUTES)):
            fd = {
                'order': queryset.id,
                'latitude': LAT_ROUTES[i],
                'longitude': LONG_ROUTES[i],
                'sequence': i+1,
            }
            serializerfd = FindingDriverSerializer(data=fd)
            if serializerfd.is_valid():
                serializerfd.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


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

class RecommendationListAPIView(ListAPIView):
    # class for get recommendation List for Passengers
    # permission_classes = [IsAuthenticated]
    serializer_class = DriversListSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(RecommendationListAPIView, self).dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        id = self.request.user.pk
        psg = Passengers.objects.filter(user=id).last()
        return Order.objects.filter(time=psg.time)

class RidingView(APIView):
    #class for change status passenger to Riding
    # permission_classes = (IsAuthenticated,)
    serializer_class = StatusUpdateSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(RidingView, self).dispatch(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        order = get_object_or_404(Order, pk=kwargs['id'])
        data = {
            'status': 'Riding'
        }
        serializer = StatusUpdateSerializer(order, data=data, partial=True)
        if serializer.is_valid():
            order = serializer.save()
            driver = Order.objects.get(id=order.pk)
            list = Passengers.objects.filter(order=order.pk, status='Accepted')
            for item in list:
                item.status = 'Arriving'
                if driver.total_psg == 2:
                    item.fee = item.fee - (item.fee * 0.1)
                elif driver.total_psg > 2:
                    item.fee = item.fee - (item.fee * 0.2)
                item.save()
            return Response(StatusUpdateSerializer(order).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

