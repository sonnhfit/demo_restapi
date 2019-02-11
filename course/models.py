from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=100)
    mota = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
