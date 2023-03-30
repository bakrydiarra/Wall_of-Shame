from .models import *
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    """
    Form to write comments
    """

    class Meta:
        model = Comment
        fields = ("content",)


class PersonaForm(forms.ModelForm):
    """
    Form to add a new persona
    """

    class Meta:
        # Get persona model and choose which fields to display
        model = Persona
        fields = (
            'shamefull_nickname', 'shameful_song',
            'shameful_tv_show', 'shameful_habit',
            'shameful_story', 'shameful_pic')
        # widgets to design input fields

        widgets = {
            'shamefull_nickname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Share a ugly nickname you have'}),
            'shameful_song': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Share a embarassing song you like'}),
            'shameful_tv_show': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Share a deplorable TV Show you like'}),
            'shameful_habit': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Share a outrageous habit you have'}),
            'shameful_story': SummernoteWidget,
        }
