"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from rest_framework_simplejwt.views import TokenRefreshView
from core.views import (
    RegistrationAPIView,LoginAPIView,LogoutAPIView,
    CreateMarksAPIView,
    CreateStudentElectiveAPIView,
    CreateAttendanceAPIView,
    StudentElectiveAPIView,
    VerificateAPIView,
    ChangePasswordAPIView,
    VerificatePasswordAPIView)
import sys
from django.conf import settings
from app.settings import DEBUG, MEDIA_URL
from django.conf.urls.static import static
sys.path.append('app/core')

urlpatterns = [
    path('api/v1/', include('core.urls')),
    path('admin/', admin.site.urls),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/registration',RegistrationAPIView.as_view(), name ='registration'),
    path('api/v1/logout',LogoutAPIView.as_view(), name ='logout'),
    path('api/v1/login',LoginAPIView.as_view(), name='login'),
    path('api/v1/createmark',CreateMarksAPIView.as_view(), name='createmark'),
    path('api/v1/createelective',CreateStudentElectiveAPIView.as_view(), name='createelective'),
    path('api/v1/createattendance',CreateAttendanceAPIView.as_view(), name='createattendance'),
    path('api/v1/studentelective/<int:id>/',StudentElectiveAPIView.as_view(), name='studentelective'),
    path('api/v1/emailverification',VerificateAPIView.as_view(), name='emailverification'),
    path('api/v1/changepassword',ChangePasswordAPIView.as_view(), name='changepassword'),
    path('api/v1/verificatepassword',VerificatePasswordAPIView.as_view(), name='verificatepassword'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
