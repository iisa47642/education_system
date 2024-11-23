from rest_framework import routers
from .views import (CoursesViewSet,CourseViewSet,ProfileViewSet,
                    ScheduleViewSet, AttendanceViewSet, RatingViewSet, ControlEventMarkViewSet)
from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView
# Создаем router и регистрируем наш ViewSet
router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet, 'profile')
router.register(r'courses', CoursesViewSet, 'courses')
router.register(r'course', CourseViewSet, 'course')
router.register(r'schedule', ScheduleViewSet, 'schedule')
router.register(r'rating', RatingViewSet, 'rating')
router.register(r'attendance', AttendanceViewSet, 'attendance')
router.register(r'marks',ControlEventMarkViewSet, 'marks')

# router.register(r'marks', MarksViewSet, 'marks')

# URLs настраиваются автоматически роутером
urlpatterns = router.urls