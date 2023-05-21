from django import forms
from .models import Gene
from .models import User
from .models import Diary


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
        

class User_Diary_Form(forms.ModelForm):
    class Meta:
        model = Diary
        fields = [
            'title', 
            'feeling_rating', 
            'diary_image',
            'diary_image2',
            'diary_image3',
            'content',
            ]
        widgets = {
            'feeling_rating': forms.RadioSelect
        }
    
class User_Gene_Register_Form_Fat(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'FTO_gene',
            'MC4R_gene',
            'BDNF_gene',
        ]
        widgets={
            'FTO_gene': forms.RadioSelect,
            'MC4R_gene': forms.RadioSelect,
            'BDNF_gene': forms.RadioSelect,
        }