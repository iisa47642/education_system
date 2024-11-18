from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from core.models import (CustomUser, Lesson, LessonLocation,
                        Subject, TypeOfLesson, StudentGroup)
from .serializers import (SubjectSerializer,CustomUserSerializer,LessonSerializer,
                          LessonLocationSerializer,TypeOfLessonSerializer,StudentGroupSerializer)


class ScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    def get_queryset(self):
        id_u = self.request.query_params.get('id')
        groups = [i.id for i in StudentGroup.objects.filter(students=id_u)]
        print(groups)
        queryset = Lesson.objects.filter(groupId__in=groups)
        return queryset

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    def get_queryset(self):
        id_u = self.request.query_params.get('id')
        queryset = CustomUser.objects.filter(id=id_u)
        return queryset

class RatingViewSet(viewsets.ModelViewSet):
    # не работает
    serializer_class = CustomUserSerializer
    def get_queryset(self):
        id_u = self.request.query_params.get('id')
        queryset = CustomUser.objects.filter(id=id_u)
        return queryset


class CourseViewSet(viewsets.ModelViewSet):
    # не работает
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
    
class CoursesViewSet(viewsets.ModelViewSet):
    # не работает
    queryset = LessonLocation.objects.all()
    serializer_class = LessonLocationSerializer

    
class AttendanceViewSet(viewsets.ModelViewSet):
    # не работает
    queryset = StudentGroup.objects.all()
    serializer_class =  StudentGroupSerializer