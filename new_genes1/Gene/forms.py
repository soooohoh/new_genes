from django import forms
from .models import Gene
from .models import User

class GeneForm(forms.ModelForm):
    class Meta:
        model = Gene
        fields = ['warnning_type', 'good_type']


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname']
        
    def signup(self, request, user):
        user.nickname = self.cleaned_data['nickname']
        user.save()