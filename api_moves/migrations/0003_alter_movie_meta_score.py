# Generated by Django 5.1.1 on 2024-09-14 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_moves', '0002_remove_movie_gross'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Meta_score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
