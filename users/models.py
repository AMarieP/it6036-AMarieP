from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    AGENT = 'AGENT'
    ADMINISTRATOR = 'ADMIN'
    MANAGMENT = 'MGMNT'

    DEPARTMENT_TYPE_CHOICES = [
    (AGENT, "Agent"),
    (ADMINISTRATOR, "Administrator"),
    (MANAGMENT, "Management"),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    department_type = models.CharField(max_length=14,
                                        choices=DEPARTMENT_TYPE_CHOICES,
                                        default=AGENT)