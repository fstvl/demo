from django.urls import  path
from . import views

urlpatterns = [
    path('df/deleteFile', views.Delete.as_view())]