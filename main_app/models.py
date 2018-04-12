from django.db import models
from django.contrib.auth.models import User
import os
def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.name), filename)

class Treasure(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    image = models.ImageField(upload_to=get_image_path, default='media/default.png')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
class Profile(models.Model):
    first_name = models.CharField(max_length=50, db_column='first_name')
    last_name = models.CharField(max_length=50, db_column='last_name')