# Generated by Django 3.0.8 on 2020-09-25 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_articletogroup_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='access_status',
            field=models.IntegerField(choices=[(0, '公开'), (1, '私有'), (2, '密码')], default=0, verbose_name='权限类型'),
        ),
    ]
