from django import forms
from .models import Gene
class GeneForm(forms.ModelForm):
    class Meta:
        model = Gene
        fields = ['warnning_type', 'good_type']
