from django import forms
from django.forms import modelformset_factory, ModelForm
from .models import Expert

DROP_DOWN_CHOICES = [
    ('name', 'Last Name'),
    ('skill', 'Skill'),
    ('class', 'Class'),
    ('organization', 'Organization')
]


class search_drop_down(forms.Form):
    search_by = forms.CharField(label='Search By', widget=forms.Select(choices=DROP_DOWN_CHOICES))
    search_term = forms.CharField(max_length=100)


expert_name_list = modelformset_factory(Expert, fields=('firstName', 'lastName', 'id'))
