# Generated by Django 4.1.3 on 2022-11-17 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_bookloan_bookload'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='Book',
            field=models.ManyToManyField(through='core.BookLoad', to='core.book'),
        ),
    ]
