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
    path('register', views.register, name = "register"),
    path('doregister', views.doregister, name = "doregister"), 
    path('login', views.login, name = "login"), 
    path('dologin', views.dologin, name = "dologin"),
    path('character/<slug:ename>/doaddbuild', views.addbuild, name = "addbuild"),
    path('character/<slug:ename>/addbuild', views.doaddbuild, name = "doaddbuild"),
    path('build/<int:iid>', views.build, name = "build"),
    path('userbuilds/<slug:login>', views.userbuilds, name = "userbuilds"),
]
