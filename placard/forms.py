from .models import *
from django import forms


class CommentForm(forms.ModelForm):
    """
    From to write comments
    """

    class Meta:
        model = Comment
        fields = ("content",)
