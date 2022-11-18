from django.urls import path, include
from django.http import HttpRequest
from . import views
app_name = "albedo"
urlpatterns=[
    path('', views.index, name = 'index'),
    path('users', views.users, name = "users"),
    path('characters', views.characters, name = "characters"),
    path('weapon', views.weapon, name = "weapon"),
    path('weapon/<slug:ename>', views.aweapon, name = "aweapon"),
    path('character/<slug:ename>', views.character, name = "character"),
]
