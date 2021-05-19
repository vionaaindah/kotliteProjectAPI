from rest_framework import serializers, viewsets, status
from rest_framework.generics import *
from passengers.serializers import *
from passengers.models import *
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated

class PassengersViewSet(viewsets.ModelViewSet):
#     permission_classes = (IsAuthenticated,)
    queryset =  Passengers.objects.all()
    serializer_class = PassengersSerializer

class PassengerDetailAPIView(ListAPIView):
    # class for get Detail Passenger
    # permission_classes = [IsAuthenticated]

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PassengerDetailAPIView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        psg = kwargs['pk']
        queryset = Passengers.objects.get(pk=psg)
        serializer = PassengersListSerializer(queryset)
        return Response(serializer.data)

class PassengersListAPIView(ListAPIView):
    # class for get List Passengers
    serializer_class = PassengersListSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PassengersListAPIView, self).dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        orders = self.kwargs['order']
        return Passengers.objects.filter(order=orders).exclude(status="Denied").exclude(status="Pending")

'''
    class for change passengers status
'''

class AcceptedView(APIView):
    #class for change status passenger to Accepted
    # permission_classes = (IsAuthenticated,)
    serializer_class = StatusUpdateSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AcceptedView, self).dispatch(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        passengers = get_object_or_404(Passengers, pk=kwargs['id'])
        data = {
            'status': 'Accepted'
        }
        serializer = StatusUpdateSerializer(passengers, data=data, partial=True)
        if serializer.is_valid():
            passengers = serializer.save()
            return Response(StatusUpdateSerializer(passengers).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeniedView(APIView):
    #class for change status passenger to Denied
    # permission_classes = (IsAuthenticated,)
    serializer_class = StatusUpdateSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(DeniedView, self).dispatch(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        passengers = get_object_or_404(Passengers, pk=kwargs['id'])
        data = {
            'status': 'Denied'
        }
        serializer = StatusUpdateSerializer(passengers, data=data, partial=True)
        if serializer.is_valid():
            passengers = serializer.save()
            return Response(StatusUpdateSerializer(passengers).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArrivingView(APIView):
    #class for change status passenger to Arriving
    # permission_classes = (IsAuthenticated,)
    serializer_class = StatusUpdateSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ArrivingView, self).dispatch(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        passengers = get_object_or_404(Passengers, pk=kwargs['id'])
        data = {
            'status': 'Arriving'
        }
        serializer = StatusUpdateSerializer(passengers, data=data, partial=True)
        if serializer.is_valid():
            passengers = serializer.save()
            return Response(StatusUpdateSerializer(passengers).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArrivedView(APIView):
    #class for change status passenger to Arrived
    # permission_classes = (IsAuthenticated,)
    serializer_class = StatusUpdateSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ArrivedView, self).dispatch(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        passengers = get_object_or_404(Passengers, pk=kwargs['id'])
        data = {
            'status': 'Arrived'
        }
        serializer = StatusUpdateSerializer(passengers, data=data, partial=True)
        if serializer.is_valid():
            passengers = serializer.save()
            return Response(StatusUpdateSerializer(passengers).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StartRideView(APIView):
    #class for change status passenger to Start Ride
    # permission_classes = (IsAuthenticated,)
    serializer_class = StatusUpdateSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(StartRideView, self).dispatch(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        passengers = get_object_or_404(Passengers, pk=kwargs['id'])
        data = {
            'status': 'Start Ride'
        }
        serializer = StatusUpdateSerializer(passengers, data=data, partial=True)
        if serializer.is_valid():
            passengers = serializer.save()
            return Response(StatusUpdateSerializer(passengers).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompleteRideView(APIView):
    #class for change status passenger to Complete Ride
    # permission_classes = (IsAuthenticated,)
    serializer_class = StatusUpdateSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CompleteRideView, self).dispatch(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        passengers = get_object_or_404(Passengers, pk=kwargs['id'])
        data = {
            'status': 'Complete Ride'
        }
        serializer = StatusUpdateSerializer(passengers, data=data, partial=True)
        if serializer.is_valid():
            passengers = serializer.save()
            return Response(StatusUpdateSerializer(passengers).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoneView(APIView):
    #class for change status passenger to Done
    # permission_classes = (IsAuthenticated,)
    serializer_class = StatusUpdateSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(DoneView, self).dispatch(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        passengers = get_object_or_404(Passengers, pk=kwargs['id'])
        data = {
            'status': 'Done'
        }
        serializer = StatusUpdateSerializer(passengers, data=data, partial=True)
        if serializer.is_valid():
            passengers = serializer.save()
            return Response(StatusUpdateSerializer(passengers).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
    end class for change passengers status
'''

class PassengerCreateAPIView(ListCreateAPIView):
    # class for create passenger
    serializer_class = PassengersSerializer
    # permission_classes = (IsAuthenticated,)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PassengerCreateAPIView, self).dispatch(request, *args, **kwargs)

    def get(self, request, format=None):
        queryset = Passengers.objects.all()

        psg = {
            'lat_pick': request.data['lat_pick'],
            'long_pick': request.data['long_pick'],
            'lat_drop': request.data['lat_drop'],
            'long_drop': request.data['long_drop'],
            'time': request.data['time'],
        }
        return Response(psg)
    
    def post(self, request, format=None):
        passenger = {
            'user': request.user.id,
            'order': request.data['order'],
            'lat_pick': request.data['lat_pick'],
            'long_pick': request.data['long_pick'],
            'lat_drop': request.data['lat_drop'],
            'long_drop': request.data['long_drop'],
            'time': request.data['time'],
            'status': 'Pending',
        }
        serializer = PassengersSerializer(data=passenger)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)