from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser 

class User(AbstractUser):
    CREATOR = "CREATOR"
    SUBSCRIBER = "SUBSCRIBER"

    ROLE_CHOICES = ( 
        (CREATOR, "Créateur"),
        (SUBSCRIBER, "Abonné"),
    )
    profile_pic = models.ImageField("Photo de profile")
    role = models.CharField(verbose_name="Role", choices=ROLE_CHOICES, max_length=30)


# # Create your models here.
# class User(AbstractUser):
#     pass


# class BaseUser(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     username = None

#     USERNAME_FIELD = "email"
#     EMAIL_FIELD = "email"
#     REQUIRED_FIELDS = ("password", "username")
