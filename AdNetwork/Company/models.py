from django.db import models

# Create your models here.
class Company(models.Model):

    legal_name = models.CharField(max_length=30)
    company_alias = models.CharField(max_length=30)
    logo = models.ImageField()
    Originator = models.CharField(max_length=30) # This will be a one-to-one with the account model later
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    trade_licence = models.FileField(default=None)

    def __str__(self):
        return self.company_alias