# Generated by Django 2.2.2 on 2019-07-03 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190630_1908'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.TextField(default='unknown user', max_length=20, verbose_name='автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='sort',
            field=models.PositiveIntegerField(default=500, verbose_name='Сортировка статей'),
        ),
    ]
