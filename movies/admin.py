from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.db import models
# Register your models here.

from .models import Movie, Genre

class MovieAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'release_date',
        'language',
        'format',
        'length',
        'certification',
        'movie_cover',
    ]
    fields = ('name',
        'release_date',
        'language',
        'format',
        'length',
        'certification',
        'movie_cover',
        'genre')
    
    formfield_overrides = {
        models.ManyToManyField: {
            'widget': CheckboxSelectMultiple 
        }
    }
    radio_fields = {'format': admin.HORIZONTAL}

admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)