from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['role', 'company', 'stage']
        widgets = {
            'role': forms.TextInput(attrs={'class': 'form-input'}),
            'company': forms.TextInput(attrs={'class': 'form-input'}),
            'stage': forms.Select(attrs={'class': 'form-select'}),
        }
