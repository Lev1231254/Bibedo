from django.db import models

# Create your models here.

class User(models.Model):
    login = models.CharField(max_length = 20, help_text = "имя пользователя")
    password = models.TextField(help_text = "пароль")

class Character(models.Model):
    name = models.TextField(help_text = "имя")
    weapon = models.TextField(help_text = "оружие")
    element = models.TextField(help_text = "стихия", default = "Гидро")
    ename = models.TextField(help_text = "имя для ссылок", default='Mona')
    link = models.TextField(default = "http://127.0.0.1:8000/albedo/character/Diluc")
    
class Weapon(models.Model):
    description = models.TextField(help_text = "описание оружия")
    typeof = models.TextField(help_text = "название оружия", default = "Меч")
    name = models.TextField(help_text = "название оружия", default = "Небесный меч")
    ename = models.TextField(help_text = "имя для ссылок", default = "SkySword")
    link = models.TextField(default = "http://127.0.0.1:8000/albedo/weapon/SkySword")
#class Build(models.Model):
    
