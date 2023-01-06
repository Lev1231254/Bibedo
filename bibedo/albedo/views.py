from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from albedo.models import *
from django.contrib.auth.models import User as Usert
from django.contrib.auth import logout, authenticate, login as logint

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
    template = loader.get_template('albedo/characters2.html')
    characters = Character.objects.all()
    context = {
        "characters": characters,
    }
    return HttpResponse(template.render(context,request))

def character(request, **kwargs):
    template = loader.get_template('albedo/character.html')
    character = Character.objects.get(ename = kwargs["ename"])
    build = Build.objects.filter(cname = character.name)
    context = {
        "character": character,
        "build": build,
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
    aweapon = Weapon.objects.get(ename = kwargs["ename"])
    context = {
        "aweapon": aweapon,
    }
    return HttpResponse(template.render(context,request))

def register(request):
    template = loader.get_template('albedo/register.html')
    context = {
    }
    return HttpResponse(template.render(context,request))    
def doregister(request):
    template = loader.get_template('albedo/register.html')
    username = request.POST['username']
    password = request.POST['password']
    Usert.objects.create_user(username,'',password)
    context = {
    }
    return HttpResponse(template.render(context,request))

def login(request):
    template = loader.get_template('albedo/login.html')
    context = {
    }
    return HttpResponse(template.render(context,request))      
def dologin(request):
    template = loader.get_template('albedo/login.html')
    username = request.POST['username']
    password = request.POST['password']    
    user = authenticate(username = username, password = password)
    if user is not None :
        logint(request, user)
    else:
        logout(request)
        logint(request, user)
    context = {
    }
    return HttpResponse(template.render(context,request))    

def addbuild(request,**kwargs):
    template = loader.get_template('albedo/addbuild.html')
    character = Character.objects.get(ename = kwargs["ename"])
    theweapon = request.POST.get('theweapon')
    sands = request.POST.get('sands')
    goblet = request.POST.get('goblet')
    circlet = request.POST.get('circlet')
    friend1 = request.POST.get('friend1')
    friend2 = request.POST.get('friend2')
    friend3 = request.POST.get('friend3')
    artiset1 = request.POST.get('artiset1')
    artiset2 = request.POST.get('artiset2')
    bname = request.POST.get('bname')
    Build.objects.create(bname = bname, author = request.user,cname = character.name, weapon = theweapon, artiset1 = artiset1, artiset2 = artiset2, flower = "HP", feather = "ATK", sands = sands, goblet = goblet, circlet = circlet, friend1 = friend1, friend2 = friend2, friend3 = friend3)        
    context = {
        "character": character,
    }
    return HttpResponse(template.render(context,request))    
def doaddbuild(request, **kwargs):
    template = loader.get_template('albedo/addbuild.html')
    character = Character.objects.get(ename = kwargs["ename"])
    weapon = Weapon.objects.filter(typeof = character.weapon)
    friends = Character.objects.all()
    sands = ["ATK%","HP%","DEF%","EM","ER%"]
    goblet = ["ATK%","HP%","DEF%","EM","Elemental Damage Bonus%","Physical Damage Bonus%"]
    circlet = ["ATK%","HP%","DEF%","EM","Heal Bonus%", "Crit Rate%", "Crit DMG%"]
    arts = Arts.objects.all()
    context = {
        "character": character,
        "weapon": weapon,
        "friends": friends,
        "sands": sands,
        "goblet": goblet,
        "circlet": circlet,
        "arts": arts,
    }
    return HttpResponse(template.render(context,request))    
#def sertain_character(request, name):
#	template = 
