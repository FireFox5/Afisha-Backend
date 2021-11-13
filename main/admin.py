from django.contrib import admin# Register your models here.
from .models import *
admin.site.register(Movie)
admin.site.register(Cinema)
admin.site.register(Genres)
admin.site.register(Review)