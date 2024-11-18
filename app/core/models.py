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

class AdditionalMaterials(models.Model):
    name = models.CharField(max_length=50)
    content = models.BinaryField()

    class Meta:
        db_table = ''
        verbose_name = 'Дополнительный материал'
        verbose_name_plural = 'Дополнительные материалы'


    def __str__(self):
        return self.name

class TypeOfLesson(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'typeoflesson'
        verbose_name = 'Тип занятия'
        verbose_name_plural = 'Тип занятий'
    
    def __str__(self):
        return self.name
    

class LessonLocation(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'lessonlocation'
        verbose_name = 'Аудитория'
        verbose_name_plural = 'Аудитории'
        
    def __str__(self):
        return self.name
'''
Model describing lesson
'''

class StudentGroup(models.Model):
    name = models.CharField(max_length=50)
    lessons = models.ManyToManyField(TypeOfLesson)
    students = models.ManyToManyField(CustomUser)

    
    class Meta:
        db_table = 'studentgroup'
        verbose_name = 'Группа студентов'
        verbose_name_plural = 'Группы студентов'
        
    def __str__(self):
        return self.name

class Test(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'test'
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return self.name


class ControlWork(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'controlwork'
        verbose_name = 'Контрольные работы'
        verbose_name_plural = 'Контрольные работы'

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=50)
    groups = models.ManyToManyField(StudentGroup)
    control_works=models.ManyToManyField(ControlWork)
    tests=models.ManyToManyField(Test)
    additional_materials = models.ManyToManyField(AdditionalMaterials)

    class Meta:
        db_table = 'subject'
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


    def __str__(self):
        return self.name



# TODO https://stackoverflow.com/questions/43118581/how-can-i-add-foreign-key-to-existing-class-in-django
class Lesson(models.Model):
    subjectId = models.ForeignKey(to=Subject,on_delete=models.CASCADE)
    groupId = models.ManyToManyField(to=StudentGroup, blank=True)
    teacherId = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE , null=True, blank=True, default=1)  # link to tutor
    number = models.IntegerField(null=True)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    type = models.ForeignKey(TypeOfLesson, on_delete=models.CASCADE)
    location = models.ForeignKey(to=LessonLocation, on_delete=models.CASCADE)
    date = models.DateField()
    
    class Meta:
        db_table = 'lesson'
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'
    


# class Schedule(models.Model):
#     lessonId = models.ForeignKey(to=Lesson, on_delete=models.CASCADE) # link to tutor's lessons
#     userId = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE) #link to tutor
#     class Meta:
#         db_table = 'schedule'
#         verbose_name = 'Расписание'
#         verbose_name_plural = 'Расписания'
#
#

class LessonArchive(models.Model):
    lessonId = models.ForeignKey(to=Lesson,on_delete=models.CASCADE)
    userId = models.ForeignKey(to=CustomUser,on_delete=models.CASCADE)
    attendance= models.BooleanField(default=False)

    class Meta:
        db_table = 'lessonarchive'
        verbose_name = 'Архив занятий'
        verbose_name_plural = 'Архив занятий'



    
        
