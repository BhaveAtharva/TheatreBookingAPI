# from django.db import models
# from phone_field import PhoneField
# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


# class UserManager(BaseUserManager):
#     def create_user(self, email, username, first_name, last_name, phone, password=None):
#         if not email:
#             raise ValueError("Users must have an email address")
#         if not username:
#             raise ValueError("Users must have a username")
#         if not first_name:
#             raise ValueError("Users must have a first name")
#         if not last_name:
#             raise ValueError("Users must have a last name")
#         if not phone:
#             raise ValueError("Users must have a phone number")

#         user = self.model(
#             email=self.normalize_email(email),
#             username=username,
#             first_name=first_name,
#             last_name=last_name,
#             phone=phone
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, password):
#         user = self.model(
#             email=self.normalize_email(email),
#             password=password,
#             username=username,
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user



# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#     )
#     username = models.CharField(max_length=30, unique=True)
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     phone = PhoneField()
#     date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
#     last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False) # a superuser

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = [ 'username' ]

#     objects = UserManager()

#     def __str__(self):
#         return self.email

#     def has_perms(self, perm, obj=None):
#         return self.is_admin
    
#     def has_module_perms(self, app_label):
#         return True
    