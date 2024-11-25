from rest_framework import routers
from .views import (
    CoursesViewSet,
    CourseViewSet,
    ProfileViewSet,
    ScheduleViewSet,
    AttendanceViewSet,
    AttendanceSubViewSet,
    RatingViewSet,
    ControlEventMarkViewSet,
    StudentsInGroupViewSet,
    ControlEventViewSet,
    TgbotScheduleViewSet,
    DateLessonsViewSet
)
from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView

# Создаем router и регистрируем наш ViewSet
router = routers.DefaultRouter()
router.register(r"profile", ProfileViewSet, "profile")
router.register(r"courses", CoursesViewSet, "courses")
router.register(r"course", CourseViewSet, "course")
router.register(r"schedule", ScheduleViewSet, "schedule")
router.register(r"rating", RatingViewSet, "rating")
router.register(r"attendance", AttendanceViewSet, "attendance")
router.register(r"attendancesub", AttendanceSubViewSet, "attendancesub")
router.register(r"marks", ControlEventMarkViewSet, "marks")
router.register(r"students", StudentsInGroupViewSet, "student")
router.register(r"controlevent", ControlEventViewSet, "controlevent")
router.register(r"tgschedule", TgbotScheduleViewSet, "tgschedule")
router.register(r"datelessons", DateLessonsViewSet, "datelessons")


# URLs настраиваются автоматически роутером
urlpatterns = router.urls
