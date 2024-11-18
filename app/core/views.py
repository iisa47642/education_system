from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from core.models import (CustomUser, Lesson, LessonLocation,
                        Subject, TypeOfLesson, StudentGroup)
from .serializers import (SubjectSerializer,CustomUserSerializer,LessonSerializer,
                          LessonLocationSerializer,TypeOfLessonSerializer,StudentGroupSerializer)

class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    def get_queryset(self):
        id_u = self.request.query_params.get('id')
        queryset = CustomUser.objects.filter(id=id_u)
        return queryset


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
class LessonLocationViewSet(viewsets.ModelViewSet):
    queryset = LessonLocation.objects.all()
    serializer_class = LessonLocationSerializer
    
class TypeOfLessonViewSet(viewsets.ModelViewSet):
    queryset = TypeOfLesson.objects.all()
    serializer_class = TypeOfLessonSerializer
    
class StudentGroupViewSet(viewsets.ModelViewSet):
    queryset = StudentGroup.objects.all()
    serializer_class =  StudentGroupSerializer