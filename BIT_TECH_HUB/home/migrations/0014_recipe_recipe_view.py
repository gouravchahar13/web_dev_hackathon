# Generated by Django 5.0 on 2023-12-17 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_recipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='Recipe_view',
            field=models.IntegerField(default=1),
        ),
    ]
