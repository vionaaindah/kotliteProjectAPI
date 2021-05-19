from drivers.serializers import *
from drivers.models import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import *
from rest_framework.views import APIView

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

