from django import forms
from .models import Gene
from .models import User


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname']
        
    def signup(self, request, user):
        user.nickname = self.cleaned_data['nickname']
        user.save()

class User_Profile_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname', 'intro', 'profile_picture', 'goals']