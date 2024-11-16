from rest_framework import routers
from .views import (SubjectViewSet,LessonLocationViewSet,LessonViewSet,
                    StudentGroupViewSet, CustomUserViewSet, TypeOfLessonViewSet)
# Создаем router и регистрируем наш ViewSet
router = routers.DefaultRouter()
router.register(r'subject', SubjectViewSet)
router.register(r'lesson', LessonViewSet)
router.register(r'custom_user', CustomUserViewSet, 'custom_user')
router.register(r'studentgroup', StudentGroupViewSet)
router.register(r'typeoflesson', TypeOfLessonViewSet)
router.register(r'lessonlocation', LessonLocationViewSet)
# URLs настраиваются автоматически роутером
urlpatterns = router.urls