# Generated by Django 5.0 on 2023-12-13 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_recipe_form_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='Recipe_Desciption',
            field=models.CharField(max_length=150),
        ),
    ]
