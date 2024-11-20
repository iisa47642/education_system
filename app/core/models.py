from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class StudentGroup(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'studentgroup'
        verbose_name = 'Группа студентов'
        verbose_name_plural = 'Группы студентов'
        
    def __str__(self):
        return self.name
class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    surname = models.CharField(max_length=50, blank=True)
    profile = models.CharField(max_length=50, blank=True)
    course = models.IntegerField(null=True)
    additional_info = models.TextField(null=True)
    gpa = models.FloatField(null=True, blank=True)
    perc = models.FloatField(null=True, blank=True)
    student_groups = models.ManyToManyField(to=StudentGroup)
    
    
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
        db_table = 'additionalmaterials'
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

class TypeOfControlEvent(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'typeofcontrolevent'
        verbose_name = 'Тип контрольного мероприятия'
        verbose_name_plural = 'Типы контрольных мероприятий'

    def __str__(self):
        return self.name


class ControlEvent(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(TypeOfControlEvent, on_delete=models.CASCADE)

    class Meta:
        db_table = 'controlevent'
        verbose_name = 'Kонтрольное мероприятие'
        verbose_name_plural = 'Контрольные мероприятия'

    class Meta:
        db_table = 'controlevent'
        verbose_name = 'Kонтрольное мероприятие'
        verbose_name_plural = 'Контрольные мероприятия'

    def __str__(self):
        return self.name

class ControlEventMark(models.Model):
    controlWorkId= models.ForeignKey(ControlEvent, on_delete=models.CASCADE)
    userId = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    mark = models.IntegerField()
    class Meta:
        db_table = 'controleventmark'
        verbose_name = 'Оценка за контрольное мероприятие'
        verbose_name_plural = 'Оценки за контрольные мероприятия'


class Subject(models.Model):
    name = models.CharField(max_length=50)
    groups = models.ManyToManyField(StudentGroup)
    control_event = models.ManyToManyField(to=ControlEvent)
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
    lesson_number = models.IntegerField(null=True)
    week_number = models.IntegerField(null=True)
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



    
        
