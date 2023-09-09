# userapp/models.py

from django.db import models


class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
