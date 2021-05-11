from django.forms import ModelForm, Textarea
from django import forms
from admin_user.models import *

class FormBook(ModelForm):
    class Meta:
        model = books
        exclude = ['id', 'image']

        widgets = {
            'title': forms.TextInput({'class': 'form-control', 'placeholder': 'Input here...'}),
            'isbn': forms.TextInput({'class': 'form-control', 'placeholder': 'Input here...'}),
            'publish_year': forms.NumberInput({'class': 'form-control', 'placeholder': 'Input here...'}),
            'stock': forms.NumberInput({'class': 'form-control', 'placeholder': 'Input here...'}),
            'writer': forms.TextInput({'class': 'form-control', 'placeholder': 'Input here...'}),
            'publisher': forms.Select({'class': 'form-select'}),
            'category': forms.Select({'class': 'form-select'}),
            'synopsis': Textarea({'rows': 5, 'class': 'form-control', 'placeholder': 'Input here...'}),
        }

class FormMember(ModelForm):
    class Meta:
        model = members
        exclude = ['id']

        widgets = {
            'name': forms.TextInput({'class': 'form-control', 'placeholder': 'Input here...'}),
            'email': forms.EmailInput({'class': 'form-control', 'placeholder': 'Input here...'}),
            'phone': forms.NumberInput({'class': 'form-control', 'placeholder': 'Input here...'}),
            'address': Textarea({'rows': 5, 'class': 'form-control', 'placeholder': 'Input here...'}),
        }

class FormPublisher(ModelForm):
    class Meta:
        model = publishers
        exclude = ['id']

        widgets = {
            'publisher': forms.TextInput({'class': 'form-control', 'placeholder': 'Input here...'}),
        }

class FormCategory(ModelForm):
    class Meta:
        model = categories
        exclude = ['id']

        widgets = {
            'category': forms.TextInput({'class': 'form-control', 'placeholder': 'Input here...'}),
        }