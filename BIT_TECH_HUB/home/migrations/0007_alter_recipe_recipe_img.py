# Generated by Django 5.0 on 2023-12-14 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_recipe_recipe_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='Recipe_Img',
            field=models.ImageField(default='null', upload_to='images/'),
        ),
    ]
