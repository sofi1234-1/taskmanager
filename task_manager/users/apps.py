from django.apps import AppConfig
from django.contrib.auth.models import AbstractUser

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
