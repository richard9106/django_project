"""create model forms to comments"""

from .models import Comments
from django import forms


class CommentForm(forms.ModelForm):
    """Creamos el modelo del formulario para comentarios"""
    class Meta:
        """hace parte de el modelo Comments en """
        model = Comments
        fields = ('body',)


