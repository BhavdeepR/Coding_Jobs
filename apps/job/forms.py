from django import forms

from .models import Job, Application

US_STATES = [
    ('', 'Select state'),
    ('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'),
    ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'),
    ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'),
    ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'),
    ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'),
    ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'),
    ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'),
    ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'),
    ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')
]

COUNTRIES = [
    ('', 'Select country'),
    ('USA', 'United States'),
    ('CAN', 'Canada'),
    ('GBR', 'United Kingdom'),
    ('IND', 'India'),
    ('AUS', 'Australia'),
    ('DEU', 'Germany'),
    ('FRA', 'France'),
    ('BRA', 'Brazil'),
    ('SGP', 'Singapore'),
    ('OTHER', 'Other')
]

class AddJobForm(forms.ModelForm):
    company_state = forms.ChoiceField(choices=US_STATES, required=False)
    company_country = forms.ChoiceField(choices=COUNTRIES, required=False)

    class Meta:
        model = Job
        fields = ['title', 'description', 'company_name', 'company_city', 'company_state', 'company_country', 'company_size']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['resume']
        widgets = {
            'resume': forms.FileInput(attrs={'accept': '.pdf,.doc,.docx'})
        }