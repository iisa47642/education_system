from django.contrib.auth.models import AbstractUser,Group
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

class Subject(models.Model):
    name = models.CharField(max_length=50);

class TypeOfLesson(models.Model):
    name = models.CharField(max_length=50);

class LessonLocation(models.Model):
    name = models.CharField(max_length=50);

'''
Model describing lesson
'''
class Lesson(models.Model):
    subjectId =models.ForeignKey(Subject, on_delete=models.CASCADE);
    groupId = models.ManyToManyField(Group, related_name="groups", blank=True);
    number = models.IntegerField(null=True);
    startTime = models.DateTimeField();
    endTime = models.DateTimeField();
    type = models.ForeignKey(TypeOfLesson, on_delete=models.CASCADE);
    location = models.ForeignKey(LessonLocation, on_delete=models.CASCADE);
    date = models.DateField();



class Schedule(models.Model):
    lessonId = models.ForeignKey(Lesson, on_delete=models.CASCADE); # link to tutor's lessons
    userId = models.ForeignKey(CustomUser, on_delete=models.CASCADE); #link to tutor




    
        
