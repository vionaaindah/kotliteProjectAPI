from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lat_start = models.DecimalField(max_digits=12, decimal_places=8)
    long_start = models.DecimalField(max_digits=12, decimal_places=8)
    lat_end = models.DecimalField(max_digits=12, decimal_places=8)
    long_end = models.DecimalField(max_digits=12, decimal_places=8)
    total_psg = models.IntegerField(default='0')
    status = models.CharField(max_length=200, default='Finding')
    time  = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    capacity = models.IntegerField(default='1')
    
    class Meta:
        db_table = 'drivers_order'
        managed = True

class FindingDriver(models.Model):
    order = models.ForeignKey(Order, related_name='findingdriver', on_delete=models.CASCADE)
    list = models.IntegerField(default='1')
    lat_start_point = models.DecimalField(max_digits=12, decimal_places=8)
    long_start_point = models.DecimalField(max_digits=12, decimal_places=8)
    lat_end_point = models.DecimalField(max_digits=12, decimal_places=8)
    long_end_point = models.DecimalField(max_digits=12, decimal_places=8)
    time  = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'drivers_findingdriver'
        managed = True
        unique_together = ['order', 'list']
        ordering = ['list']
