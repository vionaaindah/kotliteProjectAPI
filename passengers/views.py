from rest_framework import serializers, viewsets, status
from rest_framework.generics import *
from passengers.serializers import *
from passengers.models import *
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from drivers.models import *
from rest_framework.permissions import IsAuthenticated


class PassengerDetailAPIView(ListAPIView):
    # class for get Detail Passenger by id psg
    permission_classes = (IsAuthenticated,)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PassengerDetailAPIView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        ### Response

        The response always by `json`
        ```json
        {
            "id": 8,
            "user": 3,
            "first_name": "Siti Viona Indah",
            "last_name": "Swari",
            "phone": "+6285387772231",
            "lat_pick": "-6.1219085060081000",
            "long_pick": "106.7853479434830000",
            "place_pick": "Jl. Pluit Sakti II No.3,  RT.15/RW.7,  Pluit,  Kec. Penjaringan,  Kota Jkt Utara",
            "lat_drop": "-6.1452914868872900",
            "long_drop": "106.7290430129850000",
            "place_drop": "Jl. Kamal Raya No.56,  RT.1/RW.8,  Cengkareng Bar.,  Kecamatan Cengkareng,  Kota Jakarta Barat",
            "status": "Accepted",
            "time": "04-06-2021 09:10",
            "fee": 24000,
            "distance": 10175,
            "time_taken": 982,
            "order": 7,
            "driver_id": 7
        }
        ```
        """
        psg = kwargs['pk']
        queryset = Passengers.objects.get(pk=psg)
        serializer = PassengersListSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PassengersPendingListAPIView(ListAPIView):
    # class for get List Passengers that the status is pending
    serializer_class = PassengersListSerializer
    permission_classes = (IsAuthenticated,)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PassengersPendingListAPIView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        orders = self.kwargs['order']
        return Passengers.objects.filter(order=orders, status="Pending")


class PassengersListAPIView(ListAPIView):
    # class for get List Passengers that the status is not pending and denied
    serializer_class = PassengersListSerializer
    permission_classes = (IsAuthenticated,)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PassengersListAPIView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        orders = self.kwargs['order']
        return Passengers.objects.filter(order=orders).exclude(status="Denied").exclude(status="Pending")


# ====================== START CHANGE PASSENGERS STATUS ==================================

class AcceptedView(APIView):
    # class for change status passenger to Accepted
    permission_classes = (IsAuthenticated,)
    serializer_class = StatusUpdateSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AcceptedView, self).dispatch(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        ### Response

        The response always by `json`
        ```json
        {
            "status": "Accepted"
        }
        ```
        """
        passengers = get_object_or_404(Passengers, pk=kwargs['id'])
        data = {
            'status': 'Accepted'
        }
        serializer = StatusUpdateSerializer(
            passengers, data=data, partial=True)
        if serializer.is_valid():
            passengers = serializer.save()
            order = get_object_or_404(Order, pk=passengers.order.pk)
            # set the total_psg in order plus 1 when driver accepted psg
            order.total_psg += 1
            order.save()
            # change status order to full if total_psg and capacity order is same
            if order.total_psg == order.capacity:
                order.status = 'Full'
                order.save()
            return Response(StatusUpdateSerializer(passengers).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeniedView(APIView):
    # class for change status passenger to Denied
    permission_classes = (IsAuthenticated,)
    serializer_class = StatusUpdateSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(DeniedView, self).dispatch(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        ### Response

        The response always by `json`
        ```json
        {
            "status": "Denied"
        }
        ```
        """
        passengers = get_object_or_404(Passengers, pk=kwargs['id'])
        data = {
            'status': 'Denied'
        }
        serializer = StatusUpdateSerializer(
            passengers, data=data, partial=True)
        if serializer.is_valid():
            passengers = serializer.save()
            return Response(StatusUpdateSerializer(passengers).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArrivedView(APIView):
    # class for change status passenger to Arrived
    permission_classes = (IsAuthenticated,)
    serializer_class = StatusUpdateSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ArrivedView, self).dispatch(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        ### Response

        The response always by `json`
        ```json
        {
            "status": "Arrived"
        }
        ```
        """
        passengers = get_object_or_404(Passengers, pk=kwargs['id'])
        data = {
            'status': 'Arrived'
        }
        serializer = StatusUpdateSerializer(
            passengers, data=data, partial=True)
        if serializer.is_valid():
            passengers = serializer.save()
            return Response(StatusUpdateSerializer(passengers).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StartRideView(APIView):
    # class for change status passenger to Start Ride
    permission_classes = (IsAuthenticated,)
    serializer_class = StatusUpdateSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(StartRideView, self).dispatch(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        ### Response

        The response always by `json`
        ```json
        {
            "status": "Start Ride"
        }
        ```
        """
        passengers = get_object_or_404(Passengers, pk=kwargs['id'])
        data = {
            'status': 'Start Ride'
        }
        serializer = StatusUpdateSerializer(
            passengers, data=data, partial=True)
        if serializer.is_valid():
            passengers = serializer.save()
            return Response(StatusUpdateSerializer(passengers).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompleteRideView(APIView):
    # class for change status passenger to Complete Ride
    permission_classes = (IsAuthenticated,)
    serializer_class = StatusUpdateSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CompleteRideView, self).dispatch(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        ### Response
        
        The response always by `json`
        ```json
        {
            "status": "Complete Ride"
        }
        ```
        """
        passengers = get_object_or_404(Passengers, pk=kwargs['id'])
        data = {
            'status': 'Complete Ride'
        }
        serializer = StatusUpdateSerializer(
            passengers, data=data, partial=True)
        if serializer.is_valid():
            passengers = serializer.save()
            return Response(StatusUpdateSerializer(passengers).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoneView(APIView):
    # class for change status passenger to Done
    permission_classes = (IsAuthenticated,)
    serializer_class = StatusUpdateSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(DoneView, self).dispatch(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        ### Response

        The response always by `json`
        ```json
        {
            "status": "Done"
        }
        ```
        """
        passengers = get_object_or_404(Passengers, pk=kwargs['id'])
        data = {
            'status': 'Done'
        }
        serializer = StatusUpdateSerializer(
            passengers, data=data, partial=True)
        if serializer.is_valid():
            passengers = serializer.save()
            # change status order to Done if all passengers status in that order is Done
            order = get_object_or_404(Order, pk=passengers.order.pk)
            order.income = order.income + passengers.fee 
            order.save()
            total_done = Passengers.objects.filter(
                order=passengers.order.pk, status='Done').count()
            if order.total_psg == total_done:
                order.status = 'Done'
                order.save()
            return Response(StatusUpdateSerializer(passengers).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ====================== END CHANGE PASSENGERS STATUS ==================================

class PassengerCreateAPIView(APIView):
    # class for create passenger
    serializer_class = PassengersSerializer
    permission_classes = (IsAuthenticated,)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PassengerCreateAPIView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        ### Response

        The response always by `json`
        ```json
        {
            "id": 3,
            "lat_pick": "-6.1245877436108690",
            "long_pick": "106.7823677530232100",
            "lat_drop": "-6.1277543472448310",
            "long_drop": "106.7291288443025500",
            "place_pick": "Jl. Pluit Karang Permai III No.5,  RT.7/RW.16,  Pluit,  Kec. Penjaringan,  Kota Jkt Utara",
            "place_drop": "Jl. Oliander,  RT.2/RW.12,  Cengkareng Bar.,  Kecamatan Cengkareng,  Kota Jakarta Barat",
            "status": "Pending",
            "time": "4-06-2021 07:40",
            "fee": 22000,
            "distance": 9795,
            "time_taken": 1015,
            "created_at": "2021-05-30T17:54:51.065442+07:00",
            "updated_at": "2021-05-30T17:54:51.065477+07:00",
            "user": 9,
            "order": 10
        }
        ```
        """
        orders = kwargs['order']
        psg = {
            'user': request.data['user_id'],
            'lat_pick': request.data['lat_pick'],
            'long_pick': request.data['long_pick'],
            'place_pick': request.data['place_pick'],
            'lat_drop': request.data['lat_drop'],
            'long_drop': request.data['long_drop'],
            'place_drop': request.data['place_drop'],
            'time': request.data['time'],
            'distance': request.data['distance'],
            'time_taken': request.data['time_taken'],
            'fee': request.data['fee'],
            'order': orders,
            'status': 'Pending',
        }
        serializer = PassengersSerializer(data=psg)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
