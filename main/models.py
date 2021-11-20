from django.db import models
class Genres(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cinema(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.TextField(null=True,blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    cinema = models.ForeignKey(Cinema,on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genres)


    def __str__(self):
        return self.name

class Review(models.Model):

    text = models.TextField()
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.text

