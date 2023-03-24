from .models import *
from django import forms
from django_summernote.widgets import SummernoteWidget


class EnquiryForm(forms.ModelForm):
    """
    Django form to contact admin
    """

    class Meta:
        # Get a contact form model and choose which fields to display
        model = ContactForm
        fields = ('reason', 'name', 'email', 'message')
        # widgets to design input fields

        widgets = {
            'reason': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select your reason'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Give your name here'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Give your email here'
            }),
            'message': SummernoteWidget(attrs={
                'class': 'form-control',
                'placeholder': 'Leave youe message here'
            }),
        }
