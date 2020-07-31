from django.contrib import admin
from .models import Profile, Farm, CustomAnimal, Farmer

admin.site.register(Profile)
admin.site.register(Farm)
admin.site.register(CustomAnimal)
admin.site.register(Farmer)