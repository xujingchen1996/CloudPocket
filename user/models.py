from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class commonUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(blank=True, max_length=50)
    birthday = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'commonUser'
