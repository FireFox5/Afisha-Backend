# Generated by Django 3.2.7 on 2021-11-13 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_review_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='name',
            field=models.TextField(null=True),
        ),
    ]