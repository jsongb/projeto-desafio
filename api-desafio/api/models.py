from django.contrib.auth.models import User as DjangoUser
from django.db import models


class User(models.Model):
    name = models.CharField(max_length = 250)
    born_date = models.DateField()
    register = models.AutoField(primary_key = True)
    django_user = models.OneToOneField(
        DjangoUser, 
        null = False, 
        blank = False,
        on_delete = models.CASCADE, 
    )
