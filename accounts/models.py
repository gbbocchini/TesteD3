from django.db import models
from django.contrib.auth.models import User, PermissionsMixin


class Usuario(User, PermissionsMixin):
    
    verbose_name='user'

    def __str__(self):
        return "@{}".format(self.username)