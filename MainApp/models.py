from django.db import models

# Create your models here.

class Food(models.Model):
    food_id = models.IntegerField()
    food_name = models.TextField(max_length=300)
    food_price = models.IntegerField()
    food_available = models.BooleanField(default=False)
    food_image = models.ImageField(default="", upload_to='images/')
