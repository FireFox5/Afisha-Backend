# Generated by Django 3.2.7 on 2021-11-16 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_movie_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='main.Genres'),
        ),
    ]