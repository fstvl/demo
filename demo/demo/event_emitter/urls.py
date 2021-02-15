from django.urls import  path
from . import views

urlpatterns = [
    path('event/getStatusOfTriggeredEvent', views.get_status_of_triggered_event.as_view())]