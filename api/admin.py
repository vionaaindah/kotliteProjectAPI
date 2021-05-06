from django.contrib import admin
from .models import order, finding_driver, request, transaction

admin.site.register(order)
admin.site.register(finding_driver)
admin.site.register(request)
admin.site.register(transaction)
