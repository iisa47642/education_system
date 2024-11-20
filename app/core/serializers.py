from rest_framework import serializers
from core.models import (CustomUser, Lesson, LessonLocation,
                        Subject, TypeOfLesson, StudentGroup,AdditionalMaterials,
                        ControlEvent,ControlEventMark,TypeOfControlEvent,LessonArchive)


class LessonLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonLocation
        fields = ('id', 'name')

class CustomUserSerializer(serializers.ModelSerializer):
    student_groups = serializers.StringRelatedField(many=True)
    groups = serializers.StringRelatedField(many=True)
    class Meta:
        model = CustomUser
        fields = ('username','password','birth_date','surname',
                  'profile','gpa','course','perc','additional_info','groups','student_groups')


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
# class TypeOfControlEventSerializer(serializers.ModelSerializer):
#      class Meta:
#         model = ControlEvent
#         fields = ('id','name')
# class ControlEventSerializer(serializers.ModelSerializer):
#     type = TypeOfControlEventSerializer()
#     class Meta:
#         model = ControlEvent
#         fields = ('id','name','type')
class SubjectSerializer(serializers.ModelSerializer):
    groups = serializers.StringRelatedField(many=True)
    additional_materials = serializers.StringRelatedField(many=True)
    control_event = serializers.StringRelatedField(many=True)
    class Meta:
        model = Subject
        fields = ('id','name','groups',
                  'additional_materials','control_event')
        
        
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
                  'lesson_number','week_number','week_day_number','startTime','endTime','type',
                  'location','date']
        
class LessonArchiveSerializer(serializers.ModelSerializer):
    lessonId = LessonSerializer()
    userId = CustomUserSerializer()
    class Meta:
        model = LessonArchive
        fields = ('id', 'lessonId','userId','attendance')

class TypeOfControlEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfControlEvent
        fields = ('id', 'name')
    
class ControlEventSerializer(serializers.ModelSerializer):
    type = TypeOfControlEventSerializer()
    class Meta:
        model = ControlEvent
        fields = ('id', 'name','type')
    
class MarksSerializer(serializers.ModelSerializer):
    controlWorkId= ControlEventSerializer()
    userId = CustomUserSerializer()
    class Meta:
        model = ControlEventMark 
        fields = ('id', 'controlWorkId','mark')
    