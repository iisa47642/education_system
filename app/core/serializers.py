from rest_framework import serializers
from core.models import (CustomUser, Lesson, LessonLocation,
                        Subject, TypeOfLesson, StudentGroup)

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username','password','birth_date','surname',
                  'profile','gpa','course','perc','additional_info')

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('subjectId','groupId','teacherId',
                  'number','startTime','endTime','type','location','date')

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name')
        
class LessonLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonLocation
        fields = ('id', 'name')
        
class TypeOfLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfLesson
        fields = ('id', 'name')
        
class StudentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = ('id', 'name')