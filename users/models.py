from django.db import models

from django.contrib.auth.models import AbstractUser

from . import permissions

class User(AbstractUser):
    
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('editor', 'Editor'),
        ('readonly', 'ReadOnly'),
        ('external', 'External'),
    ]
    role_choices = dict(ROLE_CHOICES)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
        
        
    def has_module_perms(self, app_label):
        if self.is_superuser:
            return True
        return app_label in [
            'app',
        ]