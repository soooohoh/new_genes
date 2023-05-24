<<<<<<< HEAD
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
=======
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
    
>>>>>>> 4ca6192e24e793c4a9b51441f48dee89750917f2
