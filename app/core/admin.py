from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import (CustomUser, Lesson, LessonLocation,
                         Subject, TypeOfLesson, StudentGroup, LessonArchive,
                         AdditionalMaterials, ControlEvent, TypeOfControlEvent, ControlEventMark,
                         EmailVerification)


# Register your models here.
@admin.register(CustomUser)
class CategoriesAdmin(admin.ModelAdmin):
    exclude = ['user_permissions']
    model = CustomUser
    
admin.site.register(Lesson)
    
@admin.register(LessonLocation)
class CategoriesAdmin(admin.ModelAdmin):
    model = LessonLocation
    
# @admin.register(Schedule)
# class CategoriesAdmin(admin.ModelAdmin):
#     model = Schedule

@admin.register(Subject)
class CategoriesAdmin(admin.ModelAdmin):
    model = Subject

@admin.register(TypeOfLesson)
class CategoriesAdmin(admin.ModelAdmin):
    model = TypeOfLesson

@admin.register(StudentGroup)
class CategoriesAdmin(admin.ModelAdmin):
    model = StudentGroup

@admin.register(LessonArchive)
class LessonArchiveAdmin(admin.ModelAdmin):
    model = LessonArchive

@admin.register(AdditionalMaterials)
class AdditionalMaterials(admin.ModelAdmin):
    model = AdditionalMaterials

@admin.register(TypeOfControlEvent)
class TypeOfControlEvent(admin.ModelAdmin):
    model = TypeOfControlEvent

@admin.register(ControlEventMark)
class ControlEventMarkAdmin(admin.ModelAdmin):
    model = ControlEventMark

@admin.register(ControlEvent)
class ControlEventAdmin(admin.ModelAdmin):
    model = ControlEvent

@admin.register(EmailVerification)
class CEmailVerification(admin.ModelAdmin):
    model = EmailVerification