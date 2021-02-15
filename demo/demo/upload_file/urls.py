from django.urls import  path
from . import views

urlpatterns = [
    path('uf/uploadFile', views.Upload.as_view())]