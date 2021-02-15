from django.urls import  path
from . import views

urlpatterns = [
    path('api/newSession', views.new_session.as_view()),
    path('api/viewResults', views.view_results.as_view())
]