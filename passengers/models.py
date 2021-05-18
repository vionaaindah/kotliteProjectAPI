from django.db import models
from django.contrib.auth.models import User
from drivers.models import *

class Passengers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    lat_pick = models.DecimalField(max_digits=12, decimal_places=8)
    long_pick = models.DecimalField(max_digits=12, decimal_places=8)
    lat_drop = models.DecimalField(max_digits=12, decimal_places=8)
    long_drop = models.DecimalField(max_digits=12, decimal_places=8)
    status = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    fee = models.IntegerField()
    distance = models.CharField(max_length=200)
    time_taken = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'passengers'
        managed = True