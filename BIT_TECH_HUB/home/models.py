from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null =True, blank=True)
    Recipe_name=models.CharField(max_length=50)
    Recipe_Desciption=models.CharField( max_length=150)
    Recipe_Img=models.ImageField(default="null", upload_to='./', height_field=None, width_field=None, max_length=None)
    Recipe_view=models.IntegerField(default=1)