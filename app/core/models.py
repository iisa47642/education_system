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
        
    def __str__(self):
        return self.username

class Subject(models.Model):
    name = models.CharField(max_length=50)
<<<<<<< HEAD

class TypeOfLesson(models.Model):
    name = models.CharField(max_length=50)

class LessonLocation(models.Model):
    name = models.CharField(max_length=50)

=======
    
    class Meta:
        db_table = 'subject'
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class TypeOfLesson(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'typeoflesson'
        verbose_name = 'Тип занятия'
        verbose_name_plural = 'Типы занятий'

class LessonLocation(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'lessonlocation'
        verbose_name = 'Аудитория'
        verbose_name_plural = 'Аудитории'
        
>>>>>>> a289c8e (admin panel + models.py + admin.py + apps.py)
'''
Model describing lesson
'''

class StudentGroup(models.Model):
    name = models.CharField(max_length=50)
<<<<<<< HEAD
=======
    
    class Meta:
        db_table = 'studentgroup'
        verbose_name = 'Группа студентов'
        verbose_name_plural = 'Группы студентов'

>>>>>>> a289c8e (admin panel + models.py + admin.py + apps.py)

class Lesson(models.Model):
    subjectId =models.ForeignKey(Subject, on_delete=models.CASCADE)
    groupId = models.ManyToManyField(StudentGroup, related_name="groups", blank=True)
    number = models.IntegerField(null=True)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    type = models.ForeignKey(TypeOfLesson, on_delete=models.CASCADE)
    location = models.ForeignKey(LessonLocation, on_delete=models.CASCADE)
    date = models.DateField()
<<<<<<< HEAD
=======
    
    class Meta:
        db_table = 'lesson'
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'
>>>>>>> a289c8e (admin panel + models.py + admin.py + apps.py)



class Schedule(models.Model):
    lessonId = models.ForeignKey(Lesson, on_delete=models.CASCADE) # link to tutor's lessons
    userId = models.ForeignKey(CustomUser, on_delete=models.CASCADE) #link to tutor
<<<<<<< HEAD
=======
    class Meta:
        db_table = 'schedule'
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'

    
>>>>>>> a289c8e (admin panel + models.py + admin.py + apps.py)




    
        
