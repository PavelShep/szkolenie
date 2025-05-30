from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404
from .forms import RegistrationForm, Registration

def register_form(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'register/thanks.html')
    else:
        form = RegistrationForm()
    return render(request, 'register/form.html', {'form': form})

def registration_detail_api(request, id):
    try:
        registration = Registration.objects.get(id=id)
    except Registration.DoesNotExist:
        raise Http404("Registration not found")

    data = {
        'id': registration.id,
        'first_name': registration.first_name,
        'last_name': registration.last_name,
        'email': registration.email,
        'phone': registration.phone,
        'status': registration.status,
        'registration_date': registration.registration_date.isoformat(),
        'course': registration.course.title,
    }

    return JsonResponse(data)
