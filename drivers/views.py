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
    # class for create order from diver
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(OrderCreateAPIView, self).dispatch(request, *args, **kwargs)

    def post(self, request, format=None):
        """
        ### Response

        The response always by `json`
        ```json
        {
            "id": 7,
            "lat_start": "-6.1082283371175940",
            "long_start": "106.7789264530163400",
            "lat_end": "-6.1699315209059070",
            "long_end": "106.7311675982933800",
            "place_start": "Jl. Pluit Karang Ayu Barat No.B1,  RT.20/RW.2,  Pluit,  Kec. Penjaringan,  Kota Jkt Utara",
            "place_end": "Jl. Madrasah Blok Toraja No.71A,  RT.14/RW.4,  Rw. Buaya,  Kecamatan Cengkareng,  Kota Jakarta Barat",
            "total_psg": 0,
            "status": "Finding",
            "time": "4-06-2021 07:45",
            "capacity": 2,
            "car_type": "Nissan Juke",
            "income": 0,
            "created_at": "2021-05-30T17:26:40.252083+07:00",
            "updated_at": "2021-05-30T17:26:40.252129+07:00",
            "user": 7
        }
        ```
        """
        start_point = [request.data['lat_start'], request.data['long_start']]
        end_point = [request.data['lat_end'], request.data['long_end']]

        deptime = datetime.datetime.strptime(
            request.data['time'], '%d-%m-%Y %H:%M')

        gmaps = gmaps_init()
        direction = gmaps.directions(origin=start_point, destination=end_point,
                                     language='id', departure_time=deptime)

        # got the route, start address, and end address
        routes = direction[0]['legs'][0]['steps']
        start_address = direction[0]['legs'][0]['start_address']
        end_address = direction[0]['legs'][0]['end_address']

        # split address by ,
        start_add_save = re.split(',', start_address)
        end_add_save = re.split(',', end_address)

        # join address with , and remove the last two of list
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

        # save content to order table
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
        # get the last order from driver
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

        # save long and lat from route to finding driver table
        serializerfd = FindingDriverSerializer(data=fdcontent, many=True)
        if serializerfd.is_valid():
            serializerfd.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializerfd.errors, status=status.HTTP_400_BAD_REQUEST)


class DriverDetailAPIView(ListAPIView):
    # class for get Detail Driver
    permission_classes = (IsAuthenticated,)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(DriverDetailAPIView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        ### Response

        The response always by `json`
        ```json
        {
            "id": 7,
            "user": 7,
            "first_name": "Ferry",
            "last_name": "Pratama",
            "phone": "+6285382697201",
            "lat_start": "-6.1219085060081000",
            "long_start": "106.7853479434830000",
            "place_start": "Jl. Pluit Sakti II No.3,  RT.15/RW.7,  Pluit,  Kec. Penjaringan,  Kota Jkt Utara",
            "lat_end": "-6.1452914868872900",
            "long_end": "106.7290430129850000",
            "place_end": "Jl. Kamal Raya No.56,  RT.1/RW.8,  Cengkareng Bar.,  Kecamatan Cengkareng,  Kota Jakarta Barat",
            "status": "Done",
            "time": "04-06-2021 09:00",
            "total_psg": 1,
            "capacity": 3,
            "car_type": "Suzuki Swift",
            "income": 24000
        }
        ```
        """
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

    def post(self, request, format=None):
        """
        ### Response

        The response always by `json`
        ```json
        {
            "psg_data": {
                "user": 9,
                "lat_pick": -6.124587743610869,
                "long_pick": 106.78236775302321,
                "place_pick": "Jl. Pluit Karang Permai III No.5,  RT.7/RW.16,  Pluit,  Kec. Penjaringan,  Kota Jkt Utara",
                "lat_drop": -6.127754347244831,
                "long_drop": 106.72912884430255,
                "place_drop": "Jl. Oliander,  RT.2/RW.12,  Cengkareng Bar.,  Kecamatan Cengkareng,  Kota Jakarta Barat",
                "distance": 9795,
                "time_taken": 1015,
                "maximum_fee": 22000,
                "minimum_fee": 17600.0,
                "time": "4-06-2021 07:40",
                "status": "Pending"
            },
            "recommendations": [
                {
                    "id": 9,
                    "user": 8,
                    "first_name": "Hamonangan",
                    "last_name": "Sitorus",
                    "phone": "+6281260891439",
                    "lat_start": "-6.1215021240503580",
                    "long_start": "106.7943489389425800",
                    "place_start": "2,  Jl. Pluit Tim. Raya No.20,  RT.7/RW.9,  Pluit,  Kec. Penjaringan,  Kota Jkt Utara",
                    "lat_end": "-6.1818442245510650",
                    "long_end": "106.7288255993721000",
                    "place_end": "Jl. Lkr. Luar Barat No.55,  RT.2/RW.1,  Kembangan Sel.,  Kec. Kembangan,  Kota Jakarta Barat",
                    "status": "Finding",
                    "time": "4-06-2021 07:40",
                    "total_psg": 0,
                    "capacity": 4,
                    "car_type": "Suzuki Swift",
                    "income": 0
                },
                {
                    "id": 10,
                    "user": 6,
                    "first_name": "Bisma",
                    "last_name": "Satria Nugraha",
                    "phone": "+6285932992222",
                    "lat_start": "-6.1219085060080950",
                    "long_start": "106.7853479434829200",
                    "place_start": "Jl. Pluit Sakti II No.3,  RT.15/RW.7,  Pluit,  Kec. Penjaringan,  Kota Jkt Utara",
                    "lat_end": "-6.1452914868872925",
                    "long_end": "106.7290430129852900",
                    "place_end": "Jl. Kamal Raya No.56,  RT.1/RW.8,  Cengkareng Bar.,  Kecamatan Cengkareng,  Kota Jakarta Barat",
                    "status": "Finding",
                    "time": "4-06-2021 07:40",
                    "total_psg": 0,
                    "capacity": 4,
                    "car_type": "Suzuki Swift",
                    "income": 0
                }
            ]
        }
        ```
        """
        query = [
            [float(request.data['lat_pick']),
             float(request.data['long_pick'])],
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

        # got the distance value, duration value, start address and end address
        distance_value = direction[0]['legs'][0]['distance']['value']
        time_taken = direction[0]['legs'][0]['duration_in_traffic']['value']
        start_address = direction[0]['legs'][0]['start_address']
        end_address = direction[0]['legs'][0]['end_address']

        # split address by ,
        start_add_save = re.split(',', start_address)
        end_add_save = re.split(',', end_address)

        # join address with , and remove the last two of list
        place_pick = ', '.join(start_add_save[:-2])
        place_drop = ', '.join(end_add_save[:-2])

        # maximum fee
        km = distance_value // 1000

        if distance_value % 1000 >= 500:
            km+1

        if km == 0:
            fee = 6000
        else:
            fee = 6000 + ((km - 1) * 2000)

        # minimum fee
        min_fee = fee - (fee * 0.2)

        if len(recommendation) > 0:
            content = Order.objects.filter(id__in=recommendation)
            psg_data = {
                'user': request.user.pk,
                'lat_pick': float(request.data['lat_pick']),
                'long_pick': float(request.data['long_pick']),
                'place_pick': place_pick,
                'lat_drop': float(request.data['lat_drop']),
                'long_drop': float(request.data['long_drop']),
                'place_drop': place_drop,
                'distance': distance_value,
                'time_taken': time_taken,
                'maximum_fee': fee,
                'minimum_fee': min_fee,
                'time': request.data['time'],
                'status': 'Pending',
            }
            serializer = DriversListSerializer(data=content, many=True)
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
        """
        ### Response

        The response always by `json`
        ```json
        {
            "status": "Riding"
        }
        ```
        """
        order = get_object_or_404(Order, pk=kwargs['id'])
        data = {
            'status': 'Riding'
        }
        serializer = StatusUpdateSerializer(order, data=data, partial=True)
        if serializer.is_valid():
            order = serializer.save()
            driver = Order.objects.get(id=order.pk)
            list = Passengers.objects.filter(order=order.pk, status='Accepted')
            # change status from each passengers in this order to Arriving, and give discount if total passengers in this order more than 2
            for item in list:
                item.status = 'Arriving'
                if driver.total_psg == 2:
                    item.fee = item.fee - (item.fee * 0.1)
                elif driver.total_psg > 2:
                    item.fee = item.fee - (item.fee * 0.2)
                item.save()
            return Response(StatusUpdateSerializer(order).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OptimizeRouteAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        """
        ### Response

        The response always by `json`
        ```json
        [
            {
                "bounds": {
                    "northeast": {
                        "lat": -6.1157151,
                        "lng": 106.7875767
                    },
                    "southwest": {
                        "lat": -6.153827199999999,
                        "lng": 106.7271108
                    }
                },
                "copyrights": "Map data ©2021",
                "legs": [
                    {
                        "distance": {
                            "text": "33,3 km",
                            "value": 33306
                        },
                        "duration": {
                            "text": "1 jam 8 menit",
                            "value": 4060
                        },
                        "duration_in_traffic": {
                            "text": "1 jam 9 menit",
                            "value": 4126
                        },
                        "end_address": "Jl. Kamal Raya No.56, RT.2/RW.8, Cengkareng Bar., Kecamatan Cengkareng, Kota Jakarta Barat, Daerah Khusus Ibukota Jakarta 11730, Indonesia",
                        "end_location": {
                            "lat": -6.1322458,
                            "lng": 106.7288118
                        },
                        "start_address": "Jl. Pluit Sakti II No.3, RT.15/RW.7, Pluit, Kec. Penjaringan, Kota Jkt Utara, Daerah Khusus Ibukota Jakarta 14450, Indonesia",
                        "start_location": {
                            "lat": -6.1216574,
                            "lng": 106.7853313
                        },
                        "steps": [
                            {
                                "distance": {
                                    "text": "0,2 km",
                                    "value": 248
                                },
                                "duration": {
                                    "text": "1 menit",
                                    "value": 64
                                },
                                "end_location": {
                                    "lat": -6.1216523,
                                    "lng": 106.7875767
                                },
                                "html_instructions": "Ambil arah <b>timur</b> di <b>Jl. Pluit Sakti II</b> menuju <b>Taman Sakti</b>",
                                "polyline": {
                                    "points": "jsjd@iowjS?WAoD?yF"
                                },
                                "start_location": {
                                    "lat": -6.1216574,
                                    "lng": 106.7853313
                                },
                                "travel_mode": "DRIVING"
                            },
                            {
                                "distance": {
                                    "text": "73 m",
                                    "value": 73
                                },
                                "duration": {
                                    "text": "1 menit",
                                    "value": 19
                                },
                                "end_location": {
                                    "lat": -6.122306399999999,
                                    "lng": 106.7875519
                                },
                                "html_instructions": "Belok <b>kanan</b> ke <b>Jl. Pluit Sakti 1</b><div style=\"font-size:0.9em\">Jalan dengan pengunaan terbatas</div>",
                                "maneuver": "turn-right",
                                "polyline": {
                                    "points": "hsjd@k}wjSbCD"
                                },
                                "start_location": {
                                    "lat": -6.1216523,
                                    "lng": 106.7875767
                                },
                                "travel_mode": "DRIVING"
                            },
                        ],
                        "traffic_speed_entry": [],
                        "via_waypoint": [
                            {
                                "location": {
                                    "lat": -6.1270231,
                                    "lng": 106.7806897
                                },
                                "step_index": 7,
                                "step_interpolation": 0.5897440314292908
                            },
                            {
                                "location": {
                                    "lat": -6.1273389,
                                    "lng": 106.7287041
                                },
                                "step_index": 22,
                                "step_interpolation": 1
                            }
                        ]
                    }
                ],
                "overview_polyline": {
                    "points": "jsjd@iowjSAgE?yFbCDHfSjEI`H?jADd@@z@eHPBE`@i@nEi@|FZ?`LcAcBtOuAlMgC|A_B~@QHWJu@DSCMKWa@I[?a@^oAh@{AP{@LwA?k@WkAIe@FgArAcM[??DsA~Lw@fIW~EIfAi@lDc@xAY|@K`@]n@UZc@f@gAjA}BbCe@p@_@z@[bAOp@OfBAx@?t@BdADjAC\\J|BFz@h@zJBxBJhAvBva@RpHHfGFpDC~FQ`PMlLE|PIjMUfF[pCe@nCoCrIcFpOm@vBk@~Ag@rBK`@cBpFaAlC?dB^xFRhCHl@V`@x@n@jHnD`CnAbBlAbAd@t@f@jAj@fBh@`Dd@bD`@zALbBDzFElKa@jQIrA@@B@@@@LDJDHP?PENwABa@@C@GHaCF_CFeFF}BF}KTkBABjEbB??~ALVFJN?b@_@DKAwA{B?eA?IeDAe@iDG}DU{FgA}Bw@sBs@cAc@oGuCuC{A{Ay@{@]_AQoACqCHoADw@@s@EeAWe@SUQg@e@GK_@aAKcA@aANw@Xm@n@}@~BeA`Bo@d@Wv@e@`@[p@q@`A}A`AqBf@iAt@mBRYl@iB\\eANc@pAeEhEuMx@kC|@cDf@oC\\cELwETwSJgJBsARyRFeMQsMSmIe@eJcA}QKcAu@_Ec@sBIuAAg@TeDHmAa@_KAkA\\yCZyAV}@h@kAf@y@T]hAmAjCoBtAmAn@cATk@Lq@l@iGh@aGzB{RDm@b@}El@oFPBa@vDUlBWnCIx@P?H?SlB]dDk@pFF\\XrA@d@I|@OnAm@fB_@jAAb@F\\Vd@JHPFh@A`@Kx@a@K]@M`E}_@sFb@WlBiAhLq@tHG~@MpC_@tCg@lBo@tBg@z@m@t@iAlA}BbC{@zAQb@c@bBQdC?`@H`EC\\Dh@J|BXhFRtE@fADPPvCvAfX\\zINtHLlJOfPQxNGtGAvHGxKIzF[rE_@fCi@rBg@zAyDnLaDfKc@lA_@lA_@`BeAlDqAxDQb@?TAn@\\xEPrCHpAN`@j@l@rE~BxCxAzAx@rA`Av@d@ZJRPtAr@dBl@bCb@lC\\hD\\|FDdDIhI]vNGfD?fB?hMFlGBdDHfDB~BLh@DzIbAtG~@jFt@jM~AhIhBjBX`BPjE^pBH\\Ev@ItJS`DH`@n@Ab@I`@SVSP_@@wBBgCBuAAmBIkAIuAQaHs@wKuBiLmB{AQkAEwBKuEi@iIqA}Fe@wBKaCC}QUwA@}CMSA_ACMVwCxCw@v@"
                },
                "summary": "Jl. Lkr. Luar Barat",
                "warnings": [],
                "waypoint_order": []
            }
        ]
        ```
        """
        # get order id from link
        order_id = kwargs['order']
        # get order object
        queryset = Order.objects.get(pk=order_id)
        order = OrderSerializer(queryset)
        place_start = order.data['place_start']
        place_end = order.data['place_end']
        dtime = order.data['time']

        # get passenger for this order while they status not Denied and Pending
        psg_list = Passengers.objects.filter(order=order_id).exclude(
            status="Denied").exclude(status="Pending")
        psg_frame = read_frame(psg_list, fieldnames=[
                               'place_pick', 'place_drop'])
        psg_data = psg_frame.values

        # save place_drop and place_pick from each passengers
        psg_place = []
        for col in psg_data:
            for plc in col:
                psg_place.append('via:'+plc)

        gmaps = gmaps_init()
        time = datetime.datetime.strptime(
            dtime, '%d-%m-%Y %H:%M')

        optimize_route = gmaps.directions(origin=place_start, destination=place_end, language='id',
                                          departure_time=time, waypoints=psg_place, optimize_waypoints=True)

        return Response(data=optimize_route, status=status.HTTP_200_OK)
