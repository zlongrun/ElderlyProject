# Generated by Django 3.2 on 2021-05-27 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20210525_1116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'ordering': ['c_time'], 'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='ID_card',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='zip',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]