from django.urls import path
from forms_app.views import index, fetch_data, api_action, download_json, get_json, load_json_file, form_templates_view, message_templates_view
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('fetch_data/', fetch_data, name='fetch_data'),
    path('api_action/', api_action, name='api_action'),
    path('download_json/', download_json, name='download_json'),
    path('get_json/', get_json, name='get_json'),
    path('formTemplates/', views.form_templates_view, name='form_templates'),
    path('messageTemplates/', views.message_templates_view, name='message_templates'),
]