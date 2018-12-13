from django.contrib import admin

from .models import Crop_Details,User_Details
# Register your models here.

admin.site.register(User_Details)
admin.site.register(Crop_Details)