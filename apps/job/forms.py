from django import forms

from .models import Job, Application

class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'company_name', 'company_address', 'company_zipcode', 'company_city', 'company_state', 'company_country', 'company_size']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['resume']
        widgets = {
            'resume': forms.FileInput(attrs={'accept': '.pdf,.doc,.docx'})
        }