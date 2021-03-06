from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lat_start = models.DecimalField(max_digits=22, decimal_places=16)
    long_start = models.DecimalField(max_digits=22, decimal_places=16)
    lat_end = models.DecimalField(max_digits=22, decimal_places=16)
    long_end = models.DecimalField(max_digits=22, decimal_places=16)
    place_start = models.CharField(max_length=200, blank=True, null=True)
    place_end  = models.CharField(max_length=200, blank=True, null=True)
    total_psg = models.IntegerField()
    status = models.CharField(max_length=200)
    time  = models.CharField(max_length=200)
    capacity = models.IntegerField()
    car_type = models.CharField(max_length=200)
    income = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'drivers_order'
        managed = True

class FindingDriver(models.Model):
    order = models.ForeignKey(Order, related_name='findingdriver', on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
    sequence = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'finding_driver'
        managed = True
