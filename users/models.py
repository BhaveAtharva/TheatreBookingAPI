from django.db import models
from django.db.models.deletion import SET_NULL
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
import uuid
from mptt.models import MPTTModel, TreeForeignKey
from movies.models import Movie

class UserManager(BaseUserManager):
    
    def create_user(self, email, username, password, **other_fields):
        if not email:
            raise ValueError(_("Users must have an email address"))
        if not username:
            raise ValueError(_("Users must have a username"))

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **other_fields
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_admin', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('superuser must have is_staff=True')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser=True')
        
        if other_fields.get('is_admin') is not True:
            raise ValueError('superuser must have is_admin=True')

        return self.create_user(email, username, password, **other_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = PhoneNumberField()
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False) # a superuser

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'username' ]

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perms(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    


class UserReview(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4)
    review = models.TextField()
    rating = models.FloatField()
    review_date = models.DateTimeField(auto_now_add=True)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Movie')
    user_id = models.ForeignKey(CustomUser, null=True, on_delete=SET_NULL, verbose_name='user')

    def __str__(self):
        return str(self.user_id)


class Comments(MPTTModel):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4)
    user_review = models.ForeignKey(UserReview, null=True, on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser, null=True, on_delete=SET_NULL)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str('comment by '+str(self.user_id))
    