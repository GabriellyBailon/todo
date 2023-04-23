from django import forms

from .models import AcaoModel

class AcaoForm(forms.ModelForm):

    class Meta:
        model = AcaoModel
        fields = ('codigo', 'descricao', 'open', 'closed', 'high', 'low', 'volume')