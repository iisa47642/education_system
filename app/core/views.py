from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from core.models import (CustomUser, Lesson, LessonLocation,
                        Subject, TypeOfLesson, StudentGroup,LessonArchive)
from .serializers import (SubjectSerializer,CustomUserSerializer,LessonSerializer,
                          LessonLocationSerializer,TypeOfLessonSerializer,StudentGroupSerializer,
                          LessonArchiveSerializer)


class ScheduleViewSet(viewsets.ModelViewSet):
    # готово
    serializer_class = LessonSerializer
    def get_queryset(self):
        id_u = self.request.query_params.get('id')
        # role = CustomUser.objects.filter(id=id_u).get().groups.get()
        # role = str(role)
        # if role == 'student' or role=='teacher':
        query_groups = [j.all() for j in [i.student_groups for i in CustomUser.objects.filter(id=id_u)]][0]
        groups = [i.id for i in query_groups]
        queryset = Lesson.objects.filter(groupId__in=groups)
        return queryset

class ProfileViewSet(viewsets.ModelViewSet):
    # готово
    serializer_class = CustomUserSerializer
    def get_queryset(self):
        id_u = self.request.query_params.get('id')
        queryset = CustomUser.objects.filter(id=id_u)
        return queryset

class RatingViewSet(viewsets.ModelViewSet):
    #готово
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.filter(groups__name__icontains='student').order_by('-perc')


class CourseViewSet(viewsets.ModelViewSet):
    # готово
    serializer_class = SubjectSerializer
    def get_queryset(self):
        id_u = self.request.query_params.get('id')
        name = self.request.query_params.get('name')
        query_groups = [j.all() for j in [i.student_groups for i in CustomUser.objects.filter(id=id_u)]][0]
        groups = [i.id for i in query_groups]
        queryset = Subject.objects.filter(groups__in=groups) & Subject.objects.filter(name=name)
        return queryset
    
    
class CoursesViewSet(viewsets.ModelViewSet):
    # готово
    serializer_class = SubjectSerializer
    def get_queryset(self):
        id_u = self.request.query_params.get('id')
        query_groups = [j.all() for j in [i.student_groups for i in CustomUser.objects.filter(id=id_u)]][0]
        groups = [i.id for i in query_groups]
        queryset = Subject.objects.filter(groups__in=groups)
        return queryset

    
class AttendanceViewSet(viewsets.ModelViewSet):
    #готово
    serializer_class = LessonArchiveSerializer
    def get_queryset(self):
        id_u = self.request.query_params.get('id')
        queryset = LessonArchive.objects.filter(id=id_u)
        return queryset
    
class MarksViewSet(viewsets.ModelViewSet):
    # не работает нормально
    serializer_class = SubjectSerializer
    def get_queryset(self):
        id_u = self.request.query_params.get('id')
        query_groups = [j.all() for j in [i.student_groups for i in CustomUser.objects.filter(id=id_u)]][0]
        groups = [i.id for i in query_groups]
        queryset = Subject.objects.filter(groups__in=groups)
        return queryset
    