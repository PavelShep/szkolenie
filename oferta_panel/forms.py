from django import forms
from .models import Category, Course


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'order', 'publish']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'publish': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['category', 'title', 'description', 'hours', 'code', 'price', 'order', 'publish']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'publish': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
