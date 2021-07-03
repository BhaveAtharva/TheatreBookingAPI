from django.contrib import admin

# Register your models here.
from .models import Theatre, Screen


class TheatreAdmin(admin.ModelAdmin):
    list_display = ['name', 'screen_number',
                    'date_created', 'city', 'state_region', 'country', 'pincode', 'address']


class ScreenAdmin(admin.ModelAdmin):
    list_display = ['id', 'theatre_id', 'screen_format', 'seats', ]
    radio_fields = {'screen_format': admin.HORIZONTAL}


admin.site.register(Theatre, TheatreAdmin)
admin.site.register(Screen, ScreenAdmin)
