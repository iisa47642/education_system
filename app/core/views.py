from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout, views
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from core.utils import random
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
    EmailVerification
)
from .serializers import (
    SubjectSerializer,
    CustomUserSerializer,
    LessonSerializer,
    ControlEventMarkSerializer,
    LessonLocationSerializer,
    TypeOfLessonSerializer,
    StudentGroupSerializer,
    LessonArchiveSerializer,
    CustomUserRegistrationSerializer,
    CreateMarksSerializer,
    ControlEventSerializer,
    UpdateMarksSerializer,
    CreateStudentElectiveSerializer,
    DeleteStudentElectiveSerializer,
    CreateAttendanceSerializer,
    UpdateAttendanceSerializer
)
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.permissions import IsAuthenticated, AllowAny

# from core.permissions import Id
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from core.gpa import updateGpaAndPerc
class Id(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        id_u = self.request.query_params.get("id")
        return str(self.request.user) == str(CustomUser.objects.get(id=id_u).username)


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = CustomUserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            to_mail = user.email
            code = random()
            EmailVerification.objects.create(code=code, user=user)
            send_mail('Verification',f'Your code: {code}','isaevisa578@gmail.com',[to_mail,],fail_silently=False,)
            refresh = RefreshToken.for_user(user)  # Создание Refesh и Access
            refresh.payload.update(
                {  # Полезная информация в самом токене
                    "user_id": user.id,
                    "username": user.username,
                }
            )
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),  # Отправка на клиент
                },
                status=status.HTTP_201_CREATED,
            )

class VerificateAPIView(APIView):
    def post(self, request):
        data = request.data
        username = data["username"]
        email = CustomUser.objects.get(username=username).email
        id_u = CustomUser.objects.get(email=email).id
        code_u = EmailVerification.objects.get(user=id_u).code
        code_r = data["code"]
        if str(code_r) == str(code_u):
            CustomUser.objects.filter(id=id_u).update(is_active=True)
            return Response(
                status=status.HTTP_200_OK,
            )
        return Response(
                {"error": "Неверный код"}, status=status.HTTP_400_BAD_REQUEST
            )
        
class ChangePasswordAPIView(APIView):
        def post(self, request):
            data = request.data
            username = data["username"]
            user = CustomUser.objects.get(username=username)
            EmailVerification.objects.filter(user=user).delete()
            to_mail = user.email
            code = random()
            EmailVerification.objects.create(user=user,code=code)
            # EmailVerification.objects.filter(user=user).update(code=code)
            send_mail('Verification',f'Your code: {code}','isaevisa578@gmail.com',[to_mail,],fail_silently=False,)
            return Response(
                status=status.HTTP_200_OK,
            )

class VerificatePasswordAPIView(APIView):
    def post(self, request):
        data = request.data
        username = data["username"]
        password = data["password"]
        user = CustomUser.objects.get(username=username)
        id_u = user.id
        code_u = EmailVerification.objects.get(user=id_u).code
        code_r = data["code"]
        if str(code_r) == str(code_u):
            user.set_password(password)
            user.save()
            EmailVerification.objects.filter(user=user).delete()
            return Response(
                status=status.HTTP_200_OK,
            )
        return Response(
                {"error": "Неверный код"}, status=status.HTTP_400_BAD_REQUEST
            )

class LoginAPIView(APIView):
    def post(self, request):
        data = request.data
        username = data.get("username", None)
        password = data.get("password", None)
        if username is None or password is None:
            return Response(
                {"error": "Нужен и логин, и пароль"}, status=status.HTTP_400_BAD_REQUEST
            )
        user = authenticate(username=username, password=password)
        if user is None:
            return Response(
                {"error": "Неверные данные"}, status=status.HTTP_401_UNAUTHORIZED
            )
        refresh = RefreshToken.for_user(user)
        refresh.payload.update({"user_id": user.id, "username": user.username})
        return Response(
            {"refresh": str(refresh), "access": str(refresh.access_token)},
            status=status.HTTP_200_OK,
        )


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get(
            "refresh_token"
        )  # С клиента нужно отправить refresh token
        if not refresh_token:
            return Response(
                {"error": "Необходим Refresh token"}, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()  # Добавить его в чёрный список
        except Exception as e:
            return Response(
                {"error": "Неверный Refresh token"}, status=status.HTTP_400_BAD_REQUEST
            )
        return Response({"success": "Выход успешен"}, status=status.HTTP_200_OK)


class ScheduleViewSet(viewsets.ModelViewSet):
    # готово
    serializer_class = LessonSerializer

    def get_queryset(self):
        id_u = self.request.query_params.get("id")
        # role = CustomUser.objects.filter(id=id_u).get().groups.get()
        # role = str(role)
        # if role == 'student' or role=='teacher':
        query_groups = [
            j.all()
            for j in [i.student_groups for i in CustomUser.objects.filter(id=id_u)]
        ][0]
        groups = [i.id for i in query_groups]
        queryset = Lesson.objects.filter(groupId__in=groups)
        return queryset


class ProfileViewSet(viewsets.ModelViewSet):
    # готово
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        id_u = self.request.query_params.get("id")
        # if str(self.request.user) == str(CustomUser.objects.get(id=id_u).username):
        queryset = CustomUser.objects.filter(id=id_u)
        return queryset


class RatingViewSet(viewsets.ModelViewSet):
    # готово
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.filter(groups__name__icontains="student").order_by(
        "-gpa"
    )


class CourseViewSet(viewsets.ModelViewSet):
    # готово
    permission_classes = [IsAuthenticated]
    serializer_class = SubjectSerializer

    def get_queryset(self):
        id_u = self.request.query_params.get("id")
        ids = self.request.query_params.get("ids")
        query_groups = [
            j.all()
            for j in [i.student_groups for i in CustomUser.objects.filter(id=id_u)]
        ][0]
        groups = [i.id for i in query_groups]
        queryset = Subject.objects.filter(groups__in=groups) & Subject.objects.filter(
            id=ids
        )
        return queryset


class CoursesViewSet(viewsets.ModelViewSet):
    # готово
    permission_classes = [IsAuthenticated]
    serializer_class = SubjectSerializer

    def get_queryset(self):
        id_u = self.request.query_params.get("id")
        query_groups = [
            j.all()
            for j in [i.student_groups for i in CustomUser.objects.filter(id=id_u)]
        ][0]
        groups = [i.id for i in query_groups]
        queryset = Subject.objects.filter(groups__in=groups)
        return queryset


class AttendanceViewSet(viewsets.ModelViewSet):
    # готово
    # permission_classes = [IsAuthenticated]
    serializer_class = LessonArchiveSerializer

    def get_queryset(self):
        id_u = self.request.query_params.get("id")
        queryset = LessonArchive.objects.filter(userId=id_u)
        return queryset


class AttendanceSubViewSet(viewsets.ModelViewSet):
    # готово
    # permission_classes = [IsAuthenticated]
    serializer_class = LessonArchiveSerializer

    def get_queryset(self):
        id_u = self.request.query_params.get("id")
        ids = self.request.query_params.get("ids")
        les_id = [i.id for i in Lesson.objects.filter(subjectId=ids)]
        queryset = LessonArchive.objects.filter(userId=id_u,lessonId__in=les_id)
        return queryset


class ControlEventMarkViewSet(viewsets.ModelViewSet):
    serializer_class = ControlEventMarkSerializer

    def get_queryset(self):
        id_u = self.request.query_params.get("id")
        ids = self.request.query_params.get("ids")
        c = [i.id for i in ControlEvent.objects.filter(subjectId=ids)]
        queryset = ControlEventMark.objects.filter(
            userId=id_u
        ) & ControlEventMark.objects.filter(controlWorkId__in=c)
        return queryset


class CreateMarksAPIView(APIView):
    # готово
    def put(self, request):
        last_mark = ControlEventMark.objects.get(
            userId=request.data["userId"], controlWorkId=request.data["controlWorkId"]
        )
        serializer = UpdateMarksSerializer(data=request.data, instance=last_mark)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            updateGpaAndPerc(request.data["userId"])
            return Response(f"{request.data}", status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"error": "Введены не все данные"}, status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        serializer = CreateMarksSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            mark = serializer.save()
            updateGpaAndPerc(request.data["userId"])
            return Response(f"{request.data}", status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"error": "Введены не все данные"}, status=status.HTTP_400_BAD_REQUEST
            )


class StudentsInGroupViewSet(viewsets.ModelViewSet):
    # готово
    # permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        name = self.request.query_params.get("name")
        groupId = StudentGroup.objects.get(name=name).id
        queryset = CustomUser.objects.filter(
            student_groups=groupId, groups__name__icontains="student"
        )
        return queryset


class ControlEventViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = ControlEventSerializer

    def get_queryset(self):
        ids = self.request.query_params.get("ids")
        queryset = ControlEvent.objects.filter(subjectId=ids)
        return queryset

class CreateStudentElectiveAPIView(APIView):
    # готово
    def post(self, request):
        name = request.data["name"]
        groupId = StudentGroup.objects.get(name=name).id
        request.data["groupId"]=groupId
        serializer = CreateStudentElectiveSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            group = serializer.create(request.data)
            return Response(f"{request.data}", status=status.HTTP_201_CREATED)
        else:
            return Response(
                 {"error": "Введены не все данные"}, status=status.HTTP_400_BAD_REQUEST
            )
            
    def delete(self, request):
        name = request.data["name"]
        groupId = StudentGroup.objects.get(name=name).id
        request.data["groupId"]=groupId
        serializer = DeleteStudentElectiveSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            group = serializer.delete(request.data)
            return Response(f"{request.data}", status=status.HTTP_202_ACCEPTED)
        else:
            return Response(
                 {"error": "Введены не все данные"}, status=status.HTTP_400_BAD_REQUEST
            )
            
class CreateAttendanceAPIView(APIView):
    def post(self, request):
        serializer = CreateAttendanceSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            group = serializer.create(request.data)
            return Response(f"{request.data}", status=status.HTTP_201_CREATED)
        else:
            return Response(
                 {"error": "Введены не все данные"}, status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request):
        userId = request.data["userId"]
        date = request.data["date"]
        subjectId = request.data["subjectId"]
        type = request.data["type"]
        sub_groupsId = Subject.objects.filter(id=subjectId).values_list("groups",flat=True)
        us_groupsId = [i for i in CustomUser.objects.get(id=userId).student_groups.values_list('id',flat=True)]
        groupId = list(set(sub_groupsId) & set(us_groupsId))[0]
        lesId = Lesson.objects.get(subjectId=subjectId,date=date,groupId=groupId,type=type).id
        last_att = LessonArchive.objects.get(lessonId=lesId,userId=userId)
        serializer = UpdateAttendanceSerializer(data=request.data, instance=last_att)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(f"{request.data}", status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"error": "Введены не все данные"}, status=status.HTTP_400_BAD_REQUEST
            )

class StudentElectiveAPIView(APIView):
    
    def get(self, request, *args, **kwargs):
            id_u = kwargs.get("id", None)
            electivegroupsId = Subject.objects.filter(is_elective=True).values_list("groups",flat=True)
            us_groups = [i for i in CustomUser.objects.get(id=id_u).student_groups.values_list('id',flat=True)]
            groups = list(set(electivegroupsId) & set(us_groups))
            queryset1 = Subject.objects.filter(groups__in=groups)
            queryset2 = Subject.objects.filter(is_elective=True)
            serializer1 = SubjectSerializer(queryset1,many=True)
            serializer2 = SubjectSerializer(queryset2,many=True)
            dict1 = {'student_group': serializer1.data}
            dict2 = {'all_group': serializer2.data}
            merged_dictionary = {**dict1, **dict2}
            # if serializer1.is_valid(raise_exception=True) and serializer2.is_valid(raise_exception=True):
            return JsonResponse(merged_dictionary)
            # else:
            #     return Response(
            #      {"error": "Введены не все данные"}, status=status.HTTP_400_BAD_REQUEST
            # )



class DateLessonsViewSet(viewsets.ModelViewSet):
    # готово
    # permission_classes = [IsAuthenticated]
    serializer_class = LessonSerializer

    def get_queryset(self):
        group_name = self.request.query_params.get("name")
        ids = self.request.query_params.get("ids")
        groupId = StudentGroup.objects.get(name=group_name)
        queryset = Lesson.objects.filter(groupId=groupId,subjectId=ids)
        return queryset

class TgbotScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    def get_queryset(self):
        name = self.request.query_params.get("name")
        groupId = StudentGroup.objects.get(name=name)
        queryset = Lesson.objects.filter(groupId=groupId)
        return queryset