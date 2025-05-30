"""
URL configuration for szkolenie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from forms_app.views import form_templates_view, message_templates_view
from oferta_panel.views import categories_api, courses_api
from register.views import registration_detail_api
from issues.views import problems_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('offer-mng/', include('oferta_panel.urls')),
    path('offer/', include('oferta_publiczna.urls')),
    path('register/', include('register.urls')),
    path('issues/', include('issues.urls')),
    path('forms/', include('forms_app.urls')),
    path('formTemplates', form_templates_view, name='form_templates'),
    path('messageTemplates', message_templates_view, name='message_templates'),
    path('categories', categories_api, name='categories_api'),
    path('courses', courses_api, name='courses_api'),
    path('register/<int:id>', registration_detail_api, name='registration_detail_api'),
    path('problems', problems_api, name='problems_api'),
]
