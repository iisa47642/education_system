from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout, views
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from core.models import (
    CustomUser,
    Lesson,
    LessonLocation,
    Subject,
    TypeOfLesson,
    StudentGroup,
    LessonArchive,
    ControlEventMark,
    ControlEvent,
)
def updateGpaAndPerc(id_u):
    # here gpa updates
    gpa = 0

    query_groups = [j.all() for j in [i.student_groups for i in CustomUser.objects.filter(id=id_u)]][0]
    subjectIds = Subject.objects.filter(groups__in=query_groups).values_list("id", flat=True)
    totalNumberOfHours = sum(
        list(Subject.objects.filter(groups__in=query_groups).values_list("hours_number", flat=True)))
    for ids in subjectIds:
        c = [i.id for i in ControlEvent.objects.filter(subjectId=ids)]
        listOfMarks = list(ControlEventMark.objects.filter(userId=id_u, controlWorkId__in=c).values_list('mark', flat=True))
        meanOfMarks = sum(listOfMarks) / len(listOfMarks) if len(listOfMarks) != 0 else 0
        numberOfHours = Subject.objects.get(id=ids).hours_number
        gpa += meanOfMarks * numberOfHours / totalNumberOfHours
    student = CustomUser.objects.get(id=id_u)
    student.gpa = gpa
    student.save()

    # here perc updates
    studentIds = CustomUser.objects.filter(groups__name="student").values_list('id', flat=True)
    allStudentsNumber = CustomUser.objects.filter(groups__name="student").count()
    for studentId in studentIds:
        # gpa=CustomUser.objects.filter(id=studentId).values_list("gpa",flat=True)
        student = CustomUser.objects.get(id=studentId)
        gpa = student.gpa
        numberOfMoreStudents = CustomUser.objects.filter(groups__name="student",
                                                         gpa__gte=gpa).count()  # -1? but not sure
        perc = numberOfMoreStudents / allStudentsNumber * 100
        student.perc = perc
        student.save()