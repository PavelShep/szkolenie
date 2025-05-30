from django.shortcuts import render
from django.http import HttpResponse

def category_list(request):
    return HttpResponse("Publiczna lista kategorii")

def course_list(request, kategoria):
    return HttpResponse(f"Lista szkoleń dla kategorii: {kategoria}")

def course_detail(request, kateg):
    return HttpResponse(f"Szczegóły szkolenia dla kategorii: {kateg}")

