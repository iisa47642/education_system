from rest_framework import serializers
from core.models import (CustomUser, Lesson, LessonLocation,
                        Subject, TypeOfLesson, StudentGroup,AdditionalMaterials,Test,ControlWork)

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username','password','birth_date','surname',
                  'profile','gpa','course','perc','additional_info')


# class ControlWorkSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ControlWork
#         fields = ('id', 'name')
        
# class TestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Test
#         fields = ('id', 'name')

# class AdditionalMaterialsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AdditionalMaterials
#         fields = ('id', 'name', 'content')

class SubjectSerializer(serializers.ModelSerializer):
    groups = serializers.StringRelatedField(many=True)
    tests = serializers.StringRelatedField(many=True)
    control_works = serializers.StringRelatedField(many=True)
    additional_materials = serializers.StringRelatedField(many=True)
    class Meta:
        model = Subject
        fields = ('id','name','groups','control_works',
                  'tests','additional_materials')
        
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
        
class LessonSerializer(serializers.ModelSerializer):
    groupId = serializers.StringRelatedField(many=True)
    teacherId = CustomUserSerializer()
    subjectId = SubjectSerializer()
    location = LessonLocationSerializer()
    type = TypeOfLessonSerializer()
    class Meta:
        model = Lesson
        fields = ['subjectId','groupId','teacherId',
                  'number','startTime','endTime','type','location','date']