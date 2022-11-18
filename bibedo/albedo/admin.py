from django.contrib import admin

# Register your models here.
from .models import User
from .models import Character
from .models import Weapon
admin.site.register(Character)
admin.site.register(User)
admin.site.register(Weapon)
