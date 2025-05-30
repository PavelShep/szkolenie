import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Formularze, Szablony
import os

# JSON file path
JSON_FILE = os.path.join(settings.BASE_DIR, 'forms.json')

def load_json_file():
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def form_templates_view(request):
    data = load_json_file()
    return JsonResponse(data.get('formularze', {}), safe=False)

def message_templates_view(request):
    data = load_json_file()
    return JsonResponse(data.get('szablony', {}), safe=False)

def sync_db_to_json():
    """Synchronize database to forms.json"""
    formularze = Formularze.objects.values('form_name', 'attr_name', 'attr_value').order_by('form_name', 'position')
    szablony = Szablony.objects.values('template_name', 'template_text')

    data = {'formularze': {}, 'szablony': {}}
    for item in formularze:
        form_name = item['form_name']
        if form_name not in data['formularze']:
            data['formularze'][form_name] = {}
        data['formularze'][form_name][item['attr_name']] = item['attr_value']

    for item in szablony:
        data['szablony'][item['template_name']] = item['template_text']

    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def index(request):
    """Render the main page with forms and templates"""
    formularze = Formularze.objects.values('form_name').distinct()
    szablony = Szablony.objects.all()
    context = {
        'formularze': {item['form_name']: Formularze.objects.filter(form_name=item['form_name']).order_by('position') for item in formularze},
        'szablony': szablony
    }
    return render(request, 'forms_app/index.html', context)

@csrf_exempt
def fetch_data(request):
    """Handle AJAX requests to fetch form or template data"""
    if request.method == 'POST':
        data = json.loads(request.body)
        type_ = data.get('type')
        name = data.get('name')

        if type_ == 'formularze':
            items = Formularze.objects.filter(form_name=name).order_by('position').values('attr_name', 'attr_value')
            data = {item['attr_name']: item['attr_value'] for item in items}
            return JsonResponse(data)
        else:
            template = Szablony.objects.filter(template_name=name).first()
            return JsonResponse({'template_text': template.template_text if template else ''})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def api_action(request):
    """Handle CRUD operations and JSON synchronization"""
    if request.method == 'POST':
        data = json.loads(request.body)
        action = data.get('action')
        type_ = data.get('type')
        name = data.get('name')
        attr = data.get('attr')
        value = data.get('value')

        if action == 'delete':
            Formularze.objects.filter(form_name=name, attr_name=attr).delete()
        elif action == 'move_up':
            current = Formularze.objects.filter(form_name=name, attr_name=attr).first()
            if current and current.position > 0:
                prev = Formularze.objects.filter(form_name=name, position__lt=current.position).order_by('-position').first()
                if prev:
                    prev.position, current.position = current.position, prev.position
                    prev.save()
                    current.save()
        elif action == 'move_down':
            current = Formularze.objects.filter(form_name=name, attr_name=attr).first()
            next_item = Formularze.objects.filter(form_name=name, position__gt=current.position).order_by('position').first()
            if next_item:
                next_item.position, current.position = current.position, next_item.position
                next_item.save()
                current.save()
        elif action == 'add':
            max_position = Formularze.objects.filter(form_name=name).aggregate(max_position=models.Max('position'))['max_position'] or -1
            Formularze.objects.create(
                form_name=name,
                attr_name=attr,
                attr_value=value,
                position=max_position + 1
            )
        elif action == 'save_template':
            Szablony.objects.filter(template_name=name).update(template_text=value)

        sync_db_to_json()

        if type_ == 'formularze':
            items = Formularze.objects.filter(form_name=name).order_by('position').values('attr_name', 'attr_value')
            data = {item['attr_name']: item['attr_value'] for item in items}
            return JsonResponse({'success': True, 'data': data})
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def download_json(request):
    """Download forms.json"""
    if not os.path.exists(JSON_FILE):
        return JsonResponse({'error': 'Plik forms.json nie został znaleziony'}, status=404)
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        response = HttpResponse(f.read(), content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="forms.json"'
        return response

def get_json(request):
    """Get contents of forms.json"""
    if not os.path.exists(JSON_FILE):
        return JsonResponse({'error': 'Plik forms.json nie został znaleziony'}, status=404)
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        return JsonResponse(json.load(f))
