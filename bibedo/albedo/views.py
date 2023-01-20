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
    weapon = Weapon.objects.filter(typeof = character.weapon)
    build = Build.objects.filter(cname = character.name)
    aubuild = Build.objects.filter(cname = character.name, author = "leonchik")
    '''
    weapo = []
    for w in weapon:
        weapo.append(w.name)
    wep = []
    сou = []
    for i in range(len(weapo)):
        cou.append(0)
    for bui in build:
        wep.append(bui.weapon)
    for i in range(len(weapo)):
        cou[i]+= wep.count(weapo[i])	
    f = 0
    first = 0
    s = 0
    second = 0
    t = 0
    third = 0
    for i in range(len(cou)):
        if cou[i]>first:
            third = second
            t = s
            second = first
            s = f
            first = cou[i]
            f = i
           	
    top = [weapon[f],weapon[s],weapon[t]]
    '''
    context = {
        "character": character,
        "build": build,
        "aubuild": aubuild,
        #"top": top
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
    latb = Build.objects.latest('iid')
    iid = latb.iid + 1 
    picture = character.picture
    Build.objects.create(iid = iid, bname = bname, author = request.user,cname = character.name, weapon = theweapon, artiset1 = artiset1, artiset2 = artiset2, flower = "HP", feather = "ATK", sands = sands, goblet = goblet, circlet = circlet, friend1 = friend1, friend2 = friend2, friend3 = friend3, picture = picture)        
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
    
def build(request, **kwargs):
    template = loader.get_template('albedo/build.html')
    build = Build.objects.get(iid = kwargs["iid"])
    friend1 = Character.objects.get(name = build.friend1)
    friend2 = Character.objects.get(name = build.friend2)
    friend3 = Character.objects.get(name = build.friend3)
    character = Character.objects.get(name = build.cname)
    weapon = Weapon.objects.get(name = build.weapon)
    context = {
        "build": build,
        "character": character,
        "weapon": weapon,
        "friend1": friend1,
        "friend2": friend2,
        "friend3": friend3,
    }
    return HttpResponse(template.render(context,request))
   
  
def userbuilds(request, **kwargs):
    template = loader.get_template('albedo/userbuilds.html')
    user = Usert.objects.get(username = kwargs["login"])
    build = Build.objects.filter(author = user.username)
    
    context = {
        "build": build,
        "user": user,
    }
    return HttpResponse(template.render(context,request))  


