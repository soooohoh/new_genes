from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters
# Create your models here.

#유저모델
class User(AbstractUser):
    nickname = models.CharField(max_length=20, unique=True, null=True,
                                validators=[validate_no_special_characters])
    intro = models.TextField(null=True)
    profile_picture = models.ImageField(upload_to="profile_pics", default="default_profile_pic.jpg")
    goals = models.TextField(null=True)
    # Fat Model
    rating_FTO = [
        (1, 'TT'),
        (2, 'TA'),
        (3, 'AA')
    ]
    FTO_gene = models.IntegerField(choices=rating_FTO, default=None, null=True)
    rating_MC4R = [
        (1, 'TT'),
        (2, 'TC'),
        (3, 'CC')
    ]
    MC4R_gene = models.IntegerField(choices=rating_MC4R, default=None, null=True)
    rating_BDNF = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    BDNF_gene = models.IntegerField(choices=rating_BDNF, default=None, null=True)
    rating_OCA2=[
        (1, 'TT'),
        (2, 'TC'),
        (3, 'CC')
    ]
    OCA2_gene = models.IntegerField(choices=rating_OCA2, null=True, default=None)
    rating_MC1R = [
        (1, 'GG'),
        (2, 'GA'),
        (3, 'AA')
    ]
    MC1R_gene = models.IntegerField(choices=rating_MC1R, null=True, default=None)
    rating_chr20p11_1 = [
        (1, 'GG'),
        (2, 'GA'),
        (3, 'AA')
    ]
    chr20p11_1 = models.IntegerField(choices=rating_chr20p11_1, null=True, default=None)
    rating_chr20p11_2 = [
        (1, 'CC'),
        (2, 'CT'),
        (3, 'TT')
    ]
    chr20p11_2 = models.IntegerField(choices=rating_chr20p11_2, null=True, default=None)
    rating_IL2RA = [
        (1, 'TT'),
        (2, 'TC'),
        (3, 'CC')
    ]
    IL2RA = models.IntegerField(choices=rating_IL2RA, null=True, default=None)
    rating_HLA_DQB1 = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    HLA_DQB1 = models.IntegerField(choices=rating_HLA_DQB1, null=True, default=None)
    rating_EDAR = [
        (1, 'GG'),
        (2, 'GA'),
        (3, 'AA')
    ]
    EDAR = models.IntegerField(choices=rating_EDAR, null=True, default=None)
    rating_AGER_1 = [
        (1, 'CC'),
        (2, 'CT'),
        (3, 'TT')
    ]
    AGER_1 = models.IntegerField(choices=rating_AGER_1, null=True, default=None)
    rating_AGER_2 = [
        (1, 'GG'),
        (2, 'GA'),
        (3, 'AA')
    ]
    AGER_2 = models.IntegerField(choices=rating_AGER_2, null=True, default=None)
    rating_GCKR = [
        (1, 'CC'),
        (2, 'CT'),
        (3, 'TT')
    ]
    GCKR = models.IntegerField(choices=rating_GCKR, null=True, default=None)
    rating_ANGPTL3 = [
        (1, 'GG'),
        (2, 'GT'),
        (3, 'TT')
    ]
    ANGPTL3 = models.IntegerField(choices=rating_ANGPTL3, null=True, default=None)
    rating_TRIB1 = [
        (1, 'TT'),
        (2, 'TA'),
        (3, 'AA')
    ]
    TRIB1 = models.IntegerField(choices=rating_TRIB1, null=True, default=None)
    rating_HMGCR = [
        (1, 'AA'),
        (2, 'AT'),
        (3, 'TT')
    ]
    HMGCR = models.IntegerField(choices=rating_HMGCR, null=True, default=None)
    rating_ABO = [
        (1, 'CC'),
        (2, 'CA'),
        (3, 'AA')
    ]
    ABO = models.IntegerField(choices=rating_ABO, null=True, default=None)
    rating_LIPG = [
        (1, 'TT'),
        (2, 'TG'),
        (3, 'GG')
    ]
    LIPG = models.IntegerField(choices=rating_LIPG, null=True, default=None)
    rating_DGKB_TMEM195 = [
        (1, 'GG'),
        (2, 'GT'),
        (3, 'TT')
    ]
    DGKB_TMEM195 = models.IntegerField(choices=rating_DGKB_TMEM195, null=True, default=None)
    rating_CDKN2A_2B = [
        (1, 'CC'),
        (2, 'CT'),
        (3, 'TT')
    ]
    CDKN2A_2B = models.IntegerField(choices=rating_CDKN2A_2B, null=True, default=None)
    rating_GCK = [
        (1, 'GG'),
        (2, 'GA'),
        (3, 'AA')
    ]
    GCK = models.IntegerField(choices=rating_GCK, null=True, default=None)
    rating_GLIS3 = [
        (1, 'GG'),
        (2, 'GA'),
        (3, 'AA')
    ]
    GLIS3 = models.IntegerField(choices=rating_GLIS3, null=True, default=None)
    rating_GUCY1A3 = [
        (1, 'AA'),
        (2, 'AC'),
        (3, 'CC')
    ]
    GUCY1A3 = models.IntegerField(choices=rating_GUCY1A3, null=True, default=None)
    rating_ABCA1 = [
        (1, 'CC'),
        (2, 'CT'),
        (3, 'TT')
    ]
    ABCA1 = models.IntegerField(choices=rating_ABCA1, null=True, default=None)
    rating_FGF5 = [
        (1, 'AA'),
        (2, 'AT'),
        (3, 'TT')
    ]
    FGF5 = models.IntegerField(choices=rating_FGF5, null=True, default=None)
    rating_ATP2B1 = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    ATP2B1 = models.IntegerField(choices=rating_ATP2B1, null=True, default=None)
    rating_NPR3 = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    NPR3 = models.IntegerField(choices=rating_NPR3, null=True, default=None)
    rating_CYP17A1 = [
        (1, 'GG'),
        (2, 'GA'),
        (3, 'AA')
    ]
    CYP17A1 = models.IntegerField(choices=rating_CYP17A1, null=True, default=None)
    rating_SLC23A1_1 = [
        (1, 'CC'),
        (2, 'CT'),
        (3, 'TT')
    ]
    SLC23A1_1 = models.IntegerField(choices=rating_SLC23A1_1, null=True, default=None)
    rating_SLC23A1_2 = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    SLC23A1_2 = models.IntegerField(choices=rating_SLC23A1_2, null=True, default=None)
    rating_CYP1A1_CYP1A2 = [
        (1, 'AA'),
        (2, 'AC'),
        (3, 'CC')
    ]
    CYP1A1_CYP1A2 = models.IntegerField(choices=rating_CYP1A1_CYP1A2, null=True, default=None)
    rating_AHR = [
        (1, 'CC'),
        (2, 'CT'),
        (3, 'TT')
    ]
    AHR = models.IntegerField(choices=rating_AHR, null=True, default=None)    


    def __str__(self):
        return self.email
    

#외형적, 내형적 특성 11개
class Property(models.Model):
    title = models.CharField(max_length=50)
    descript = models.TextField()

#유전자 종류
class Gene(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=10, primary_key=True)
    description = models.TextField()
    warnning_type = models.CharField(max_length=2, null=True)
    middle_type = models.CharField(max_length=2, null=True)
    good_type = models.CharField(max_length=2, null=True)
    


#생활습관, 식습관

class Eating_Habits(models.Model):
    gene_name = models.CharField(max_length=13, null=True)
    food_name = models.CharField(max_length=20, null=True)
    food_description = models.TextField(null=True)
    foods = models.TextField(null=True)


class LifeStyle(models.Model):
    gene_name = models.CharField(max_length=20)
    style = models.TextField()
    
    #다이어리
class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True)
    rating = [
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★')
    ]
    feeling_rating = models.IntegerField(choices=rating, default=None)
    diary_image = models.ImageField(upload_to="diary_pics")
    diary_image2 = models.ImageField(upload_to="diary_pics", blank = True)
    diary_image3 = models.ImageField(upload_to="diary_pics", blank = True)
    content = models.TextField()
    dt_created = models.DateField(auto_now_add=True)
    dt_updated = models.DateField(auto_now=True)
    

    