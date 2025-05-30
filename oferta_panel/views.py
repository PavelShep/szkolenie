from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CategoryForm, CourseForm
from django.http import JsonResponse
from .models import Category, Course

@login_required
def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'oferta_panel/category_thanks.html')
    else:
        form = CategoryForm()
    return render(request, 'oferta_panel/category_form.html', {'form': form})

@login_required
def course_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'oferta_panel/course_thanks.html')
    else:
        form = CourseForm()
    return render(request, 'oferta_panel/course_form.html', {'form': form})

def categories_api(request):
    categories = Category.objects.filter(publish=True).order_by('order')
    data = [
        {
            'id': category.id,
            'name': category.name,
            'order': category.order,
        }
        for category in categories
    ]
    return JsonResponse(data, safe=False)

from .models import Course

def courses_api(request):
    courses = Course.objects.filter(publish=True).order_by('order')
    data = [
        {
            'id': course.id,
            'title': course.title,
            'description': course.description,
            'hours': course.hours,
            'code': course.code,
            'price': str(course.price),  # Decimal to string
            'order': course.order,
            'category': course.category.name
        }
        for course in courses
    ]
    return JsonResponse(data, safe=False)
