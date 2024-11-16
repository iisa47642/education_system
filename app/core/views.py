from django.shortcuts import render

from rest_framework import viewsets
from core.models import (CustomUser, Lesson, LessonLocation,
                        Subject, TypeOfLesson, StudentGroup)
from .serializers import (SubjectSerializer,CustomUserSerializer,LessonSerializer,
                          LessonLocationSerializer,TypeOfLessonSerializer,StudentGroupSerializer)

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all(filter)
    serializer_class = CustomUserSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class =  LessonSerializer
    
class LessonLocationViewSet(viewsets.ModelViewSet):
    queryset = LessonLocation.objects.all()
    serializer_class = LessonLocationSerializer
    
class TypeOfLessonViewSet(viewsets.ModelViewSet):
    queryset = TypeOfLesson.objects.all()
    serializer_class = TypeOfLessonSerializer
    
class StudentGroupViewSet(viewsets.ModelViewSet):
    queryset = StudentGroup.objects.all()
    serializer_class =  StudentGroupSerializer