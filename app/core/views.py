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
        role = CustomUser.objects.filter(id=id_u).get().groups.get()
        role = str(role)
        if role == 'student':
            query_groups = [j.all() for j in [i.student_groups for i in CustomUser.objects.filter(id=id_u)]][0]
            groups = [i.id for i in query_groups]
        queryset = Lesson.objects.filter(groupId__in=groups)
        return queryset

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    def get_queryset(self):
        id_u = self.request.query_params.get('id')
        queryset = CustomUser.objects.filter(id=id_u)
        return queryset

class RatingViewSet(viewsets.ModelViewSet):
    
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.filter(groups=1).order_by('-gpa')


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    def get_queryset(self):
        id_u = self.request.query_params.get('id')
        name = self.request.query_params.get('name')
        groups = [i.id for i in StudentGroup.objects.filter(students=id_u)]
        queryset = Subject.objects.filter(groups__in=groups) & Subject.objects.filter(name=name)
        return queryset
    
    
class CoursesViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    def get_queryset(self):
        id_u = self.request.query_params.get('id')
        groups = [i.id for i in StudentGroup.objects.filter(students=id_u)]
        queryset = Subject.objects.filter(groups__in=groups)
        return queryset

    
class AttendanceViewSet(viewsets.ModelViewSet):
    # не работает
    
    queryset = StudentGroup.objects.all()
    serializer_class =  StudentGroupSerializer