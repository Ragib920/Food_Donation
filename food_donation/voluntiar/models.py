from django.db import models
from django.utils import timezone
from  django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

class volentiar(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    email = models.EmailField( max_length=60, unique = True)
    user_name = models.CharField (max_length=60)
    password1 = models.CharField(max_length=60)
    password2 = models.CharField(max_length=60)

    def __str__(self):
        return self.firstname

