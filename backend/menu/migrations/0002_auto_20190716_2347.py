# Generated by Django 2.2.2 on 2019-07-16 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsmenu',
            name='url',
            field=models.CharField(max_length=255, verbose_name='Ссылка на внешний ресурс'),
        ),
    ]