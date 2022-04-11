from django.urls import path
from . import views

urlpatterns = [
  path('createRecord', views.createRecord, name="createRecord")
] 