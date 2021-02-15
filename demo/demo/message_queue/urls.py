from django.urls import  path
from . import views

urlpatterns = [
    path('mq/publishMessage', views.publish_message.as_view())]