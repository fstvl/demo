from django.urls import  path
from . import views

urlpatterns = [
    path('runtest', views.run_test_api.as_view()),
    path('df/download', views.download_zip.as_view())]