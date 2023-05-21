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
    # Fat Form
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
    