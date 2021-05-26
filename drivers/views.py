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

from modules.SimpleTF import TFNearestNeighbor
from django_pandas.io import read_frame
from maps_env import gmaps_init
from geopy import distance
import pandas as pd
import datetime
import re

class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(OrderCreateAPIView, self).dispatch(request, *args, **kwargs)

    def post(self, request, format=None):
        # TODO : edit the order model
        start_point = [request.data['lat_start'], request.data['long_start']]
        end_point = [request.data['lat_end'], request.data['long_end']]

        deptime = datetime.datetime.strptime(
            request.data['time'], '%d-%m-%Y %H:%M')

        gmaps = gmaps_init()
        direction = gmaps.directions(origin=start_point, destination=end_point,
                                    language='id', departure_time=deptime)
        routes = direction[0]['legs'][0]['steps']

        start_address = direction[0]['legs'][0]['start_address']
        end_address = direction[0]['legs'][0]['end_address']

        # adress = 'lt 4, Lippo Plaza Batu, Jl. Diponegoro No.1, Sisir, Kec. Batu, Kota Batu, Jawa Timur 65314, Indonesia'
        start_add_save = re.split(',', start_address)
        end_add_save = re.split(',', end_address)

        # result = ['lt 4', 'Lippo Plaza Batu', 'Jl. Diponegoro No.1', 'Sisir', 'Kec. Batu', Kota Batu,'Jawa Timur 65314', 'Indonesia']
        place_start = ', '.join(start_add_save[:-2])
        place_end = ', '.join(end_add_save[:-2])

        content = {
            'user': request.user.id,
            'lat_start': start_point[0],
            'long_start': start_point[1],
            'lat_end': end_point[0],
            'long_end': end_point[1],
            'total_psg': 0,
            'income': 0,
            'status': 'Finding',
            'time': request.data['time'],
            'capacity': request.data['capacity'],
            'car_type': request.data['car_type'],
            'place_start': place_start,
            'place_end': place_end
        }

        serializer = OrderSerializer(data=content)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        LAT_ROUTES = []
        LONG_ROUTES = []

        LAT_ROUTES.append(request.data['lat_start'])
        LONG_ROUTES.append(request.data['long_start'])

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

        LAT_ROUTES.append(request.data['lat_end'])
        LONG_ROUTES.append(request.data['long_end'])

        id = request.user.pk
        queryset = Order.objects.filter(user=id).last()
        fdcontent = []

        for i in range(len(LAT_ROUTES)):
            fd = {
                'order': queryset.id,
                'latitude': LAT_ROUTES[i],
                'longitude': LONG_ROUTES[i],
                'sequence': i+1,
            }
            fdcontent.append(fd)

        # TO DO : Mungkin disini bis di cek lagi deh
        serializerfd = FindingDriverSerializer(data=fdcontent, many=True)
        if serializerfd.is_valid():
            serializerfd.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializerfd.errors, status=status.HTTP_400_BAD_REQUEST)


class DriverDetailAPIView(ListAPIView):
    # class for get Detail Driver
    permission_classes = (IsAuthenticated,)

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
    permission_classes = (IsAuthenticated,)
    serializer_class = DriversListSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(RecommendationListAPIView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        id = self.request.user.pk
        psg = Passengers.objects.filter(user=id).last()
        return Order.objects.filter(time=psg.time)

    def post(self, request, format=None):
        """
        request = {
            'pickup_lat': lat,
            'pickup_long': long,
            'dropoff_lat': lat,
            'dropoff_long': long,
            'pickup_time': '25-06-2021 15:45',
        }
        """
        query = [
            [float(request.data['lat_pick']), float(request.data['long_pick'])],
            [float(request.data['lat_drop']), float(request.data['long_drop'])]
        ]
        time = pd.to_datetime(request.data['time'])

        # get all order data and make it to dataframe
        data_order = Order.objects.all()
        df = read_frame(data_order,
                        fieldnames=['id', 'user_id', 'status', 'time'])
        df['time'] = pd.to_datetime(df['time'])

        # create filter data
        delta = datetime.timedelta(minutes=15)
        aboveth = time + delta
        lowerth = time - delta

        # filter data
        df = df.loc[(df['time'] <= aboveth) & (df['time'] >= lowerth)]
        df = df.loc[df['status'] == 'Finding']

        dist = []

        for dt in df.values:
            # dt[0] >> id order
            data_drv = FindingDriver.objects.filter(order_id=dt[0])
            train = read_frame(data_drv, fieldnames=['latitude', 'longitude'])
            train = train.values

            model = TFNearestNeighbor()
            model.fit_transform(train, query)

            if model.indices[0] < model.indices[1]:
                dist.append((model.values[0] + model.values[1], dt[0],
                             train[model.indices[0]], train[model.indices[1]]))

        sorted_dist = sorted(dist)
        recommendation = []

        for sd in sorted_dist:
            pick_dist = distance.distance(query[0], sd[2]).km
            drop_dist = distance.distance(query[1], sd[3]).km
            if (pick_dist <= 0.7) & (drop_dist <= 0.7):
                recommendation.append(sd[1])

        # direction API
        start_point = [request.data['lat_pick'], request.data['long_pick']]
        end_point = [request.data['lat_drop'], request.data['long_drop']]

        deptime = datetime.datetime.strptime(
            request.data['time'], '%d-%m-%Y %H:%M')
        gmaps = gmaps_init()
        direction = gmaps.directions(origin=start_point, destination=end_point,
                                    language='id', departure_time=deptime)

        start_address = direction[0]['legs'][0]['start_address']
        end_address = direction[0]['legs'][0]['end_address']

        # adress = 'lt 4, Lippo Plaza Batu, Jl. Diponegoro No.1, Sisir, Kec. Batu, Kota Batu, Jawa Timur 65314, Indonesia'
        start_add_save = re.split(',', start_address)
        end_add_save = re.split(',', end_address)

        # result = ['lt 4', 'Lippo Plaza Batu', 'Jl. Diponegoro No.1', 'Sisir', 'Kec. Batu', Kota Batu,'Jawa Timur 65314', 'Indonesia']
        place_pick = ', '.join(start_add_save[:-2])
        place_drop = ', '.join(end_add_save[:-2])

        # sampai sini dapat id ordernya dalam bentuk list, gimana cara dapetin data dari list id order
        # [1,2,3,4]
        if len(recommendation) > 0:
            content = Order.objects.filter(id__in=recommendation)
            psg_data = {
                'user': request.user.pk,
                'lat_pick': float(request.data['lat_pick']),
                'long_pick': float(request.data['long_pick']),
                'lat_drop': float(request.data['lat_drop']),
                'long_drop': float(request.data['long_drop']),
                'place_pick': place_pick,
                'place_drop':place_drop,
                'time': request.data['time'],
                'status': 'Pending',
            }
            serializer = OrderSerializer(data=content, many=True)
            serializer.is_valid()
            data_return = {
                'psg_data': psg_data,
                'recommendations': serializer.data
            }
            return Response(data=data_return, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


class RidingView(APIView):
    # class for change status passenger to Riding
    permission_classes = (IsAuthenticated,)
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
