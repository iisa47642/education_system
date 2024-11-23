from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from django.contrib.auth import authenticate,login,logout,views
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from core.models import (CustomUser, Lesson, LessonLocation,
                        Subject, TypeOfLesson, StudentGroup,LessonArchive, ControlEventMark)
from .serializers import (SubjectSerializer,CustomUserSerializer,LessonSerializer,ControlEventMarkSerializer,
                          LessonLocationSerializer,TypeOfLessonSerializer,StudentGroupSerializer,
                          LessonArchiveSerializer,CustomUserRegistrationSerializer)
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.permissions import IsAuthenticated,AllowAny
# from core.permissions import Id
from rest_framework import permissions

class Id(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        id_u = self.request.query_params.get('id')
        return str(self.request.user) == str(CustomUser.objects.get(id=id_u).username)
class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = CustomUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user) # Создание Refesh и Access
            refresh.payload.update({    # Полезная информация в самом токене
                'user_id': user.id,
                'username': user.username
            })
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),       # Отправка на клиент
            }, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)
        if username is None or password is None:
            return Response({'error': 'Нужен и логин, и пароль'},
                            status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'error': 'Неверные данные'},
                            status=status.HTTP_401_UNAUTHORIZED)
        refresh = RefreshToken.for_user(user)
        refresh.payload.update({
            'user_id': user.id,
            'username': user.username
        })
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }, status=status.HTTP_200_OK)
        
class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        refresh_token = request.data.get('refresh_token') # С клиента нужно отправить refresh token
        if not refresh_token:
            return Response({'error': 'Необходим Refresh token'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist() # Добавить его в чёрный список
        except Exception as e:
            return Response({'error': 'Неверный Refresh token'},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response({'success': 'Выход успешен'}, status=status.HTTP_200_OK)

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
    ermission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer
    def get_queryset(self):
        id_u = self.request.query_params.get('id')
        if str(self.request.user) == str(CustomUser.objects.get(id=id_u).username):
            queryset = CustomUser.objects.filter(id=id_u)
            return queryset
            

class RatingViewSet(viewsets.ModelViewSet):
    #готово
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.filter(groups__name__icontains='student').order_by('-perc')


class CourseViewSet(viewsets.ModelViewSet):
    # готово
    permission_classes = [IsAuthenticated]
    serializer_class = SubjectSerializer
    def get_queryset(self):
        id_u = self.request.query_params.get('id')
        ids = self.request.query_params.get('ids')
        query_groups = [j.all() for j in [i.student_groups for i in CustomUser.objects.filter(id=id_u)]][0]
        groups = [i.id for i in query_groups]
        queryset = Subject.objects.filter(groups__in=groups) & Subject.objects.filter(id=ids)
        return queryset
    
    
class CoursesViewSet(viewsets.ModelViewSet):
    # готово
    permission_classes = [IsAuthenticated]
    serializer_class = SubjectSerializer
    def get_queryset(self):
        id_u = self.request.query_params.get('id')
        query_groups = [j.all() for j in [i.student_groups for i in CustomUser.objects.filter(id=id_u)]][0]
        groups = [i.id for i in query_groups]
        queryset = Subject.objects.filter(groups__in=groups)
        return queryset

    
class AttendanceViewSet(viewsets.ModelViewSet):
    #готово
    permission_classes = [IsAuthenticated]
    serializer_class = LessonArchiveSerializer
    def get_queryset(self):
        id_u = self.request.query_params.get('id')
        queryset = LessonArchive.objects.filter(id=id_u)
        return queryset
    
class ControlEventMarkViewSet(viewsets.ModelViewSet):
    # не работает нормально
    serializer_class = ControlEventMarkSerializer
    def get_queryset(self):
        id_u = self.request.query_params.get('id')
        ids = self.request.query_params.get('ids')
        conids = [j.all() for j in [i.control_event for i in Subject.objects.filter(id=ids)]][0]
        c = [i.id for i in conids]
        queryset =  ControlEventMark.objects.filter(userId=id_u) & ControlEventMark.objects.filter(controlWorkId__in=c)
        return queryset
    