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
    bigpicture = models.TextField(default = "https://paimon.moe/images/characters/full/mona.png")
    rarity = models.IntegerField(default='5')
    elepic = models.TextField(default = "https://paimon.moe/images/elements/gydro.png")
    raripic = models.TextField(default = "https://static.wikia.nocookie.net/genshin-impact/images/6/69/%D0%98%D0%BA%D0%BE%D0%BD%D0%BA%D0%B0_5_%D0%97%D0%B2%D1%91%D0%B7%D0%B4.png/revision/latest/scale-to-width-down/79?cb=20210226153349&path-prefix=ru")
    region = models.TextField(default = "Мондштадт")
    color = models.TextField(default = "")
class Build(models.Model):
	iid = models.IntegerField(default='0')
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
	picture = models.TextField(default = "https://paimon.moe/images/characters/mona.png")
    
    
class Weapon(models.Model):
    description = models.TextField(help_text = "описание оружия")
    typeof = models.TextField(help_text = "тип оружия", default = "Катализатор")
    name = models.TextField(help_text = "название оружия", default = "Песнь Странника")
    ename = models.TextField(help_text = "имя для ссылок", default = "TheWidsith")
    picture = models.TextField(default = "https://paimon.moe/images/weapons/the_widsith.png")

class Arts(models.Model):
	name = models.TextField(help_text = "имя", default='Эмблема рассечённой судьбы')
	flower = models.TextField(default= 'https://paimon.moe/images/artifacts/crimson_witch_of_flames_flower.png')
	feather = models.TextField(default='https://paimon.moe/images/artifacts/crimson_witch_of_flames_feather.png')
	sands = models.TextField(default='https://paimon.moe/images/artifacts/crimson_witch_of_flames_sands.png')
	goblet = models.TextField(default='https://paimon.moe/images/artifacts/crimson_witch_of_flames_goblet.png')
	circlet = models.TextField(default='https://paimon.moe/images/artifacts/crimson_witch_of_flames_circlet.png')
#class Sands(models.Model):
#	char = models.TextField(help_text = "характеристика", default='ATK%')

#class Goblet(models.Model):
#	char = models.TextField(help_text = "характеристика", default='Elemental Damage Bonus%')
	
#class Circlet(models.Model):
#	char = models.TextField(help_text = "характеристика", default='Crit Rate%')
	


