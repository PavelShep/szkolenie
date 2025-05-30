from django.urls import path
from . import views

urlpatterns = [
    path('', views.issue_form, name='issue_form'),
]
