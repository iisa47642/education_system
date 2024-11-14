from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    surname = models.CharField(max_length=50, blank=True)
    profile = models.CharField(max_length=50, blank=True)
    course = models.IntegerField(null=True)
    additional_info = models.TextField(null=True)
    gpa = models.FloatField(null=True, blank=True)
    perc = models.FloatField(null=True, blank=True)
    
    class Meta:
        db_table = 'custom_user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        
    
        
