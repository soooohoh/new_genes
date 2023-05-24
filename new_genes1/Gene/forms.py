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
    
class User_Gene_Register_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'FTO_gene', 'chr20p11_1',
            'MC4R_gene', 'chr20p11_2',
            'BDNF_gene', 'IL2RA',
            'OCA2_gene', 'HLA_DQB1',
            'MC1R_gene', 'EDAR',
            'AGER_1', 'AGER_2',
            'GCKR', 'ANGPTL3',
            'TRIB1', 'HMGCR',
            'ABCA1', 'ABO',
            'LIPG', 'DGKB_TMEM195',
            'CDKN2A_2B', 'GCK',
            'GLIS3', 'GUCY1A3',
            'FGF5', 'ATP2B1',
            'NPR3', 'CYP17A1',
            'SLC23A1_1', 'SLC23A1_2',
            'CYP1A1_CYP1A2',
            'AHR'
        ]
        widgets={
            'ABCA1': forms.RadioSelect,
            'FTO_gene': forms.RadioSelect,
            'MC4R_gene': forms.RadioSelect,
            'BDNF_gene': forms.RadioSelect,
            'OCA2_gene': forms.RadioSelect,
            'MC1R_gene': forms.RadioSelect,
            'AGER_1': forms.RadioSelect,
            'GCKR': forms.RadioSelect,
            'TRIB1': forms.RadioSelect,
            'ABO': forms.RadioSelect,
            'LIPG': forms.RadioSelect,
            'CDKN2A_2B': forms.RadioSelect,
            'GLIS3': forms.RadioSelect,
            'FGF5': forms.RadioSelect,
            'NPR3': forms.RadioSelect,
            'SLC23A1_1': forms.RadioSelect,
            'CYP1A1_CYP1A2': forms.RadioSelect,
            'chr20p11_1': forms.RadioSelect,
            'chr20p11_2': forms.RadioSelect,
            'IL2RA': forms.RadioSelect,
            'HLA_DQB1': forms.RadioSelect,
            'EDAR': forms.RadioSelect,
            'AGER_2': forms.RadioSelect,
            'ANGPTL3': forms.RadioSelect,
            'HMGCR': forms.RadioSelect,
            'DGKB_TMEM195': forms.RadioSelect,
            'GCK': forms.RadioSelect,
            'GUCY1A3': forms.RadioSelect,
            'ATP2B1': forms.RadioSelect,
            'CYP17A1': forms.RadioSelect,
            'SLC23A1_2': forms.RadioSelect,
            'CYP1A1_CYP1A2': forms.RadioSelect,
            'AHR': forms.RadioSelect
        }
