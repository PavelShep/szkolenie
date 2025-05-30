from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_form, name='register_form'),
]
