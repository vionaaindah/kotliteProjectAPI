from django.db import models
from django.contrib.auth.models import User
from drivers.models import *

class request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    lat_pick = models.DecimalField(max_digits=9, decimal_places=8)
    long_pick = models.DecimalField(max_digits=9, decimal_places=8)
    lat_drop = models.DecimalField(max_digits=9, decimal_places=8)
    long_drop = models.DecimalField(max_digits=9, decimal_places=8)
    status = models.CharField(max_length=200)
    waktu = models.DateTimeField()
    class Meta:
        db_table = 'request'

class transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request = models.ForeignKey(request, on_delete=models.CASCADE)
    status = models.CharField(max_length=200)
    fee = models.IntegerField()
    class Meta:
        db_table = 'transaction'