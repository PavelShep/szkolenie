from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='public_category_list'),
    path('<str:kategoria>', views.course_list, name='public_course_list'),
    path('<str:kateg>/course', views.course_detail, name='course_detail'),
]
