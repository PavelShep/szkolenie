from django.urls import path
from oferta_panel.views import categories_api
from . import views

urlpatterns = [
    path('categ-add', views.category_add, name='category_add'),
    path('course-add', views.course_add, name='course_add'),
    path('categories', categories_api, name='categories_api'),
]
