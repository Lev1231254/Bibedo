from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from albedo.models import User
from albedo.models import Character
from albedo.models import Weapon

def index(request):
    template = loader.get_template('albedo/mainpage.html')
    context = {
        "a": 1,
    }
    return HttpResponse(template.render(context, request))    

def users(request):
    template = loader.get_template('albedo/users.html')
    users = User.objects.all()
    context = {
        "users": users,
    }
    return HttpResponse(template.render(context, request))
# Create your views here.

def characters(request):
    template = loader.get_template('albedo/characters.html')
    characters = Character.objects.all()
    context = {
        "characters": characters,
    }
    return HttpResponse(template.render(context,request))

def character(request, **kwargs):
    template = loader.get_template('albedo/character.html')
    character = Character.objects.get(ename = kwargs["ename"])
    context = {
        "character": character,
    }
    return HttpResponse(template.render(context,request))
    
def weapon(request):
    template = loader.get_template('albedo/weapon.html')
    weapon = Weapon.objects.all()
    context = {
        "weapon": weapon,
    }
    return HttpResponse(template.render(context,request))

def aweapon(request, **kwargs):
    template = loader.get_template('albedo/aweapon.html')
    weapon = Weapon.objects.get(ename = kwargs["ename"])
    context = {
        "weapon": weapon,
    }
    return HttpResponse(template.render(context,request))
#def sertain_character(request, name):
#	template = 
