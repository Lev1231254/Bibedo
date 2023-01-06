from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Character)
admin.site.register(User)
admin.site.register(Weapon)
admin.site.register(Build)
admin.site.register(Arts)
