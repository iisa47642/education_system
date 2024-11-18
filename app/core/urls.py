from rest_framework import routers
from .views import (CoursesViewSet,CourseViewSet,ProfileViewSet,
                    ScheduleViewSet, AttendanceViewSet, RatingViewSet)
# Создаем router и регистрируем наш ViewSet
router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet, 'profile')
router.register(r'courses', CoursesViewSet, 'courses')
router.register(r'course', CourseViewSet, 'course')
router.register(r'shedule', ScheduleViewSet, 'shedule')
router.register(r'typeoflesson', RatingViewSet, 'rating')
router.register(r'lessonlocation', AttendanceViewSet, 'attendance')
# URLs настраиваются автоматически роутером
urlpatterns = router.urls