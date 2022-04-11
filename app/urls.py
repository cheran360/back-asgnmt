from django.urls import path
from . import views

urlpatterns = [
  path('application', views.sample, name='sample'),
  path('createRecord', views.createRecord, name="createRecord")
] 