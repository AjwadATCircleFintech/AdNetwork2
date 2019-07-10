from django.db import models
from django.contrib.auth.models import  AbstractUser


class Accounts(AbstractUser):



     activate = models.BooleanField()
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)