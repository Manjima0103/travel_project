from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=250)
    des = models.TextField()
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=250)
    des = models.TextField()
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name


class Pic(models.Model):
    img = models.ImageField(upload_to='pics')



