from django.db import models
from django.contrib.auth.models import User
from drivers.models import *

class Passengers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    lat_pick = models.DecimalField(max_digits=22, decimal_places=16)
    long_pick = models.DecimalField(max_digits=22, decimal_places=16)
    lat_drop = models.DecimalField(max_digits=22, decimal_places=16)
    long_drop = models.DecimalField(max_digits=22, decimal_places=16)
    status = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    fee = models.IntegerField(blank=True, null=True)
    distance = models.IntegerField(blank=True, null=True)
    time_taken = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'passengers'
        managed = True