# Generated by Django 4.1.3 on 2023-01-13 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albedo', '0019_remove_weapon_link_alter_weapon_typeof'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='iid',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='character',
            name='picture',
            field=models.TextField(default='https://paimon.moe/images/characters/mona.png'),
        ),
    ]
