from rest_framework import serializers
from core.models import (CustomUser, Lesson, LessonLocation,
                        Subject, TypeOfLesson, StudentGroup,AdditionalMaterials,
                        ControlEvent,ControlEventMark,TypeOfControlEvent,LessonArchive)


class LessonLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonLocation
        fields = ('id', 'name')
class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username','password','email')
        
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        user.set_password(validated_data['password'])
        return user
class CustomUserSerializer(serializers.ModelSerializer):

    student_groups = serializers.StringRelatedField(many=True)
    groups = serializers.StringRelatedField(many=True)
    groups = serializers.StringRelatedField(many=True)
    class Meta:
        model = CustomUser
        fields = ('username','password','birth_date','surname',
                  'profile','gpa','course','perc','additional_info','groups','student_groups','email')
        # fields = ('username','password',
        #           'email')


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
    # control_event = serializers.StringRelatedField(many=True)
    class Meta:
        model = Subject
        fields = ('id','name','groups',
                  'additional_materials','is_elective')
        
        
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
    
class ControlEventMarkSerializer(serializers.ModelSerializer):
    controlWorkId = ControlEventSerializer()
    # userId = CustomUserSerializer()
    class Meta:
        model = ControlEventMark 
        fields = ('id','controlWorkId','mark')
    
class CreateMarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlEventMark
        fields = ('controlWorkId','userId','mark')
        
    def create(self, validated_data):
        mark = CustomUser.objects.create(
            validated_data['controlWorkId'],
            validated_data['userId'],
            validated_data['mark']
        )
        return mark