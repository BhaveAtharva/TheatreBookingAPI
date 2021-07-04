from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.db import models
from django.contrib.auth.models import Group
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()
# admin.site.unregister(Group)

class CustomUserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm


    list_display = [
        'username',
        'first_name',
        'last_name',
        'email',
        'phone',
        'date_joined',
        'last_login',
        'is_active',
        'is_admin',
        'is_staff',
        'is_superuser',
    ]
    # fields = (
    #     'username',
    #     'first_name',
    #     'last_name',
    #     'phone',
    #     'is_active',
    #     'is_admin',
    #     'is_staff',
    #     'is_superuser',
    # )

    fieldsets = ( 
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username','first_name','last_name','phone')}),
        ('Permissions', {'fields': ('is_active','is_admin','is_staff','is_superuser', 'groups')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password', 'password_2')}
        ),
    )

    formfield_overrides = {
        models.ManyToManyField: {
            'widget': CheckboxSelectMultiple 
        }
    }




admin.site.register(CustomUser, CustomUserAdmin)