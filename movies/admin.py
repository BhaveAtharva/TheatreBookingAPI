# from django.contrib import admin
# from django.forms import CheckboxSelectMultiple
# from django.db import models
# # Register your models here.

# from .models import Language, Movie, Genre


# class MovieAdmin(admin.ModelAdmin):

#     list_display = [
#         'id',
#         'name',
#         'release_date',
#         'language',
#         'format',
#         'length',
#         'certification',
#         'movie_cover',
#         'genres'
#     ]
#     fields = ('name',
#               'release_date',
#               'language',
#               'format',
#               'length',
#               'certification',
#               'movie_cover',
#               'genre')

#     def genres(self, obj):
#         genres = obj.genre.all()
#         genres = ', '.join([str(i) for i in genres])
#         return genres

#     formfield_overrides = {
#         models.ManyToManyField: {
#             'widget': CheckboxSelectMultiple
#         }
#     }
#     radio_fields = {'format': admin.HORIZONTAL}


# class MovieInline(admin.TabularInline):
#     model = Movie.genre.through


# class GenreAdmin(admin.ModelAdmin):
#     model = Genre
#     inlines = [
#         MovieInline
#     ]


# class LanguagesAdmin(admin.ModelAdmin):
#     model = Language
#     fields = ['language_code', 'language_name', ]


# admin.site.register(Language, LanguagesAdmin)
# admin.site.register(Movie, MovieAdmin)
# admin.site.register(Genre)
