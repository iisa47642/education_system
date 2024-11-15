from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import (CustomUser, Lesson, LessonLocation,
                         Schedule, Subject, TypeOfLesson, StudentGroup)


# Register your models here.
@admin.register(CustomUser)
class CategoriesAdmin(admin.ModelAdmin):
    model = CustomUser

admin.site.register(Lesson)
    
@admin.register(LessonLocation)
class CategoriesAdmin(admin.ModelAdmin):
    model = LessonLocation
    
@admin.register(Schedule)
class CategoriesAdmin(admin.ModelAdmin):
    model = Schedule

@admin.register(Subject)
class CategoriesAdmin(admin.ModelAdmin):
    model = Subject

@admin.register(TypeOfLesson)
class CategoriesAdmin(admin.ModelAdmin):
    model = TypeOfLesson

@admin.register(StudentGroup)
class CategoriesAdmin(admin.ModelAdmin):
    model = StudentGroup