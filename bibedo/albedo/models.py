from django.db import models
from django.contrib.auth.forms import User
# Create your models here.


class User(models.Model):
    login = models.CharField(max_length = 20, help_text = "имя пользователя")
    password = models.TextField(help_text = "пароль")
    

class Character(models.Model):
    name = models.TextField(help_text = "имя")
    weapon = models.TextField(help_text = "оружие")
    element = models.TextField(help_text = "стихия", default = "Гидро")
    ename = models.TextField(help_text = "имя для ссылок", default='Mona')
    picture = models.TextField(default = "https://paimon.moe/images/characters/mona.png")

class Build(models.Model):
	bname = models.TextField(help_text = "название билда", default='название')
	author = models.TextField(help_text = "автор", default='leonchik')
	cname = models.TextField(help_text = "имя персонажа", default='Мона')
	weapon = models.TextField(help_text = "оружие", default='TheWidsith')
	artiset1 = models.TextField(help_text = "сет артефактов1", default='Эмблема рассечённой судьбы')
	artiset2 = models.TextField(help_text = "сет артефактов2", default='Эмблема рассечённой судьбы')
	flower = models.TextField(help_text = "цветок", default='HP')
	feather = models.TextField(help_text = "перо", default='ATK')
	sands = models.TextField(help_text = "часы", default='ATK%')
	goblet = models.TextField(help_text = "кубан", default='Elemental Damage Bonus%')
	circlet = models.TextField(help_text = "корона", default='Crit Rate%')
	friend1 = models.TextField(help_text = "союзник 1", default='Дилюк')
	friend2 = models.TextField(help_text = "союзник 2", default='Джин')
	friend3 = models.TextField(help_text = "союзник 3", default='Ке Цин')
    
    
class Weapon(models.Model):
    description = models.TextField(help_text = "описание оружия")
    typeof = models.TextField(help_text = "тип оружия", default = "Катализатор")
    name = models.TextField(help_text = "название оружия", default = "Песнь Странника")
    ename = models.TextField(help_text = "имя для ссылок", default = "TheWidsith")

class Arts(models.Model):
	name = models.TextField(help_text = "имя", default='Эмблема рассечённой судьбы')
	
#class Sands(models.Model):
#	char = models.TextField(help_text = "характеристика", default='ATK%')

#class Goblet(models.Model):
#	char = models.TextField(help_text = "характеристика", default='Elemental Damage Bonus%')
	
#class Circlet(models.Model):
#	char = models.TextField(help_text = "характеристика", default='Crit Rate%')
	


