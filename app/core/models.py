from django.db import models

class Store(models.Model):
    id_store = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name

class User(models.Model):

    pass