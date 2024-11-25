from rest_framework import serializers
from core.models import (
    CustomUser,
    Lesson,
    LessonLocation,
    Subject,
    TypeOfLesson,
    StudentGroup,
    AdditionalMaterials,
    ControlEvent,
    ControlEventMark,
    TypeOfControlEvent,
    LessonArchive,
)


class LessonLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonLocation
        fields = ("id", "name")


class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("username", "password", "email")

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"],
        )
        user.set_password(validated_data["password"])
        return user


class CustomUserSerializer(serializers.ModelSerializer):

    student_groups = serializers.StringRelatedField(many=True)
    groups = serializers.StringRelatedField(many=True)
    groups = serializers.StringRelatedField(many=True)

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "password",
            "birth_date",
            "surname",
            "profile",
            "gpa",
            "course",
            "perc",
            "additional_info",
            "groups",
            "student_groups",
            "email",
        )


class SubjectSerializer(serializers.ModelSerializer):
    groups = serializers.StringRelatedField(many=True)
    additional_materials = serializers.StringRelatedField(many=True)

    # control_event = serializers.StringRelatedField(many=True)
    class Meta:
        model = Subject
        fields = ("id", "name", "groups", "additional_materials", "is_elective")


class TypeOfLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfLesson
        fields = ("id", "name")


class StudentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = ("id", "name")


class LessonSerializer(serializers.ModelSerializer):
    groupId = serializers.StringRelatedField(many=True)
    teacherId = CustomUserSerializer()
    subjectId = SubjectSerializer()
    location = LessonLocationSerializer()
    type = TypeOfLessonSerializer()

    class Meta:
        model = Lesson
        fields = [
            "subjectId",
            "groupId",
            "teacherId",
            "lesson_number",
            "week_number",
            "week_day_number",
            "startTime",
            "endTime",
      
      "type",
            "location",
            "date",
        ]


class LessonArchiveSerializer(serializers.ModelSerializer):
    lessonId = LessonSerializer()
    userId = CustomUserSerializer()

    class Meta:
        model = LessonArchive
        fields = ("id", "lessonId", "userId", "attendance")


# class LessonSubSerializer(serializers.ModelSerializer):


class TypeOfControlEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfControlEvent
        fields = ("id", "name")


class ControlEventSerializer(serializers.ModelSerializer):
    type = TypeOfControlEventSerializer()

    class Meta:
        model = ControlEvent
        fields = ("id", "name", "type")


class ControlEventMarkSerializer(serializers.ModelSerializer):
    controlWorkId = ControlEventSerializer()

    # userId = CustomUserSerializer()
    class Meta:
        model = ControlEventMark
        fields = ("id", "controlWorkId", "mark")


class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id",)


class ControlEventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlEvent
        fields = ("id",)

class CreateMarksSerializer(serializers.ModelSerializer):
    userId = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    controlWorkId = serializers.PrimaryKeyRelatedField(
        queryset=ControlEvent.objects.all()
    )

    class Meta:
        model = ControlEventMark
        fields = ("controlWorkId", "userId", "mark")

    def create(self, validated_data):
        mark = ControlEventMark.objects.create(**validated_data)
        return mark


class UpdateMarksSerializer(serializers.ModelSerializer):
    userId = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    controlWorkId = serializers.PrimaryKeyRelatedField(
        queryset=ControlEvent.objects.all()
    )

    class Meta:
        model = ControlEventMark
        fields = ("id", "controlWorkId", "userId", "mark")

    def update(self, instance, validated_data):
        instance.mark = validated_data.get("mark", instance.mark)
        instance.save()
        return instance

class CreateStudentElectiveSerializer(serializers.Serializer):
    userId = serializers.IntegerField()
    groupId = serializers.IntegerField()
    
    def create(self, validated_data):
        userId = validated_data["userId"]
        groupId = validated_data["groupId"]
        student = CustomUser.objects.get(id=userId)
        group = StudentGroup.objects.get(id=groupId)
        query = student.student_groups.add(group)
        return query

class DeleteStudentElectiveSerializer(serializers.Serializer):
    userId = serializers.IntegerField()
    groupId = serializers.IntegerField()
    
    def delete(self, validated_data):
        userId = validated_data["userId"]
        groupId = validated_data["groupId"]
        student = CustomUser.objects.get(id=userId)
        group = StudentGroup.objects.get(id=groupId)
        query = student.student_groups.remove(group)
        return query

        
        
class CreateAttendanceSerializer(serializers.Serializer):
    userId = serializers.IntegerField()
    groupId = serializers.IntegerField()
    date = serializers.DateField()
    subjectId = serializers.IntegerField()
    attendance = serializers.BooleanField()
    type = serializers.IntegerField()
    
    
    def create(self, validated_data):
        userId = validated_data["userId"]
        groupId = validated_data["groupId"]
        date = validated_data["date"]
        subjectId = validated_data["subjectId"]
        type = validated_data["type"]
        attendance = validated_data["attendance"]
        # lesId = Lesson.objects.get(subjectId=subjectId,date=date,groupId=groupId,type=type).id
        query = LessonArchive.objects.create(lessonId=Lesson.objects.get(subjectId=subjectId,date=date,groupId=groupId,type=type),userId=CustomUser.objects.get(id=userId),attendance=attendance)
        return query    
        
class UpdateAttendanceSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        instance.attendance = validated_data.get("attendance", instance.attendance)
        instance.save()
        return instance