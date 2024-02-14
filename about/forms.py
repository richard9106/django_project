"""importamos los modelos de about """

from .models import CollaborateRequest
from django import forms


class CollaborateForm(forms.ModelForm):
    """ Create the model for collaborateForm"""
    class Meta:
        """We select the files to apear in the form"""
        model = CollaborateRequest
        fields = ('name', 'email', 'message',)
