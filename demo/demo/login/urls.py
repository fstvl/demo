from django.urls import  path
from . import views

urlpatterns = [
    path('auth/login', views.login_api.as_view()),
    path('auth/change-password', views.change_password.as_view())
]