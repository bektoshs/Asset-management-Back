from django.contrib import admin
from .models import Employee, Department, Device, Location

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Device)
admin.site.register(Location)
