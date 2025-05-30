from django import forms
from .models import IssueReport

class IssueReportForm(forms.ModelForm):
    class Meta:
        model = IssueReport
        fields = ['author', 'subject', 'description']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
