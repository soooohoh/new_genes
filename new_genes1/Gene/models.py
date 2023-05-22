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
    FTO_gene = models.IntegerField(choices=rating_FTO, default=None, null=True,)
    rating_MC4R = [
        (1, 'TT'),
        (2, 'TC'),
        (3, 'CC')
    ]
    MC4R_gene = models.IntegerField(choices=rating_MC4R, default=None, null=True,)
    rating_BDNF = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    BDNF_gene = models.IntegerField(choices=rating_BDNF, default=None, null=True, )
    rating_OCA2 = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    OCA2_gene = models.IntegerField(choices=rating_OCA2, default=None)
    rating_MC1R = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    MC1R_gene = models.IntegerField(choices=rating_MC1R, default=None)
    rating_chr20p11_1 = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    chr20p11_1 = models.IntegerField(choices=rating_chr20p11_1, default=None)
    rating_chr20p11_2 = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    chr20p11_2 = models.IntegerField(choices=rating_chr20p11_2, default=None)
    rating_IL2RA = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    IL2RA = models.IntegerField(choices=rating_IL2RA, default=None)
    rating_HLA_DQB1 = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    HLA_DQB1 = models.IntegerField(choices=rating_HLA_DQB1, default=None)
    rating_EDAR = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    EDAR = models.IntegerField(choices=rating_EDAR, default=None)
    rating_AGER_1 = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    AGER_1 = models.IntegerField(choices=rating_AGER_1, default=None)
    rating_AGER_2 = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    AGER_2 = models.IntegerField(choices=rating_AGER_2, default=None)
    rating_GCKR = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    GCKR = models.IntegerField(choices=rating_GCKR, default=None)
    rating_ANGPTL3 = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    ANGPTL3 = models.IntegerField(choices=rating_ANGPTL3, default=None)
    rating_TRIB1 = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    TRIB1 = models.IntegerField(choices=rating_TRIB1, default=None)
    rating_HMGCR = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    HMGCR = models.IntegerField(choices=rating_HMGCR, default=None)
    rating_ABO = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    ABO = models.IntegerField(choices=rating_ABO, default=None)
    rating_ABCA1 = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    ABCA1 = models.IntegerField(choices=rating_ABCA1, default=None)
    rating_LIPG = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    LIPG = models.IntegerField(choices=rating_LIPG, default=None)
    rating_DGKB_TMEM195 = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    DGKB_TMEM195 = models.IntegerField(choices=rating_DGKB_TMEM195, default=None)
    rating_CDKN2A_2B = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    CDKN2A_2B = models.IntegerField(choices=rating_CDKN2A_2B, default=None)
    rating_GCK = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    GCK = models.IntegerField(choices=rating_GCK, default=None)
    rating_GLIS3 = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    GLIS3 = models.IntegerField(choices=rating_GLIS3, default=None)
    rating_GUCY1A3 = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    GUCY1A3 = models.IntegerField(choices=rating_GUCY1A3, default=None)
    rating_FGF5 = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    FGF5 = models.IntegerField(choices=rating_FGF5, default=None)
    rating_ATP2B1 = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    ATP2B1 = models.IntegerField(choices=rating_ATP2B1, default=None)
    rating_NPR3 = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    NPR3 = models.IntegerField(choices=rating_NPR3, default=None)
    rating_CYP17A1 = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    CYP17A1 = models.IntegerField(choices=rating_CYP17A1, default=None)
    rating_SLC23A1_1 = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    SLC23A1_1 = models.IntegerField(choices=rating_SLC23A1_1, default=None)
    rating_SLC23A1_2 = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    SLC23A1_2 = models.IntegerField(choices=rating_SLC23A1_2, default=None)
    rating_CYP1A1_CYP1A2 = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]
    CYP1A1_CYP1A2 = models.IntegerField(choices=rating_CYP1A1_CYP1A2, default=None)
    rating_AHR = [
        (1, 'AA'),
        (2, 'AG'),
        (3, 'GG')
    ]           


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
    

    