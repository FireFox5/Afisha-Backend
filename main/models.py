from django.db import models
class Genres(models.Model):
    name = models.CharField(max_length=100,null=True)
class Cinema(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.TextField(null=True,blank=True)
    description = models.CharField(max_length=100)
    cinema = models.ForeignKey(Cinema,on_delete=models.CASCADE,null=True)
    genres = models.ManyToManyField(Genres,null=True,blank=True)


class Review(models.Model):
    text = models.TextField(null=True,blank=True)
    # movie = models.ForeignKey()

