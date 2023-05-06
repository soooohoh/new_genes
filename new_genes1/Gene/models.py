from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters
# Create your models here.

#외형적, 내형적 특성 11개
class Property(models.Model):
    title = models.CharField(max_length=50)
    descript = models.TextField()


#유전자 종류
class Gene(models.Model):
    property_id = models.ForeignKey(Property, related_name="property", on_delete=models.CASCADE, db_column="property_id", null=True)
    name = models.CharField(max_length=10, primary_key=True)
    description = models.TextField()
    type = models.CharField(max_length=2)
#생활습관, 식습관

class Eating_Habits(models.Model):
    gene_name = models.CharField(max_length=13, null=True)
    food_name = models.CharField(max_length=20, null=True)
    food_description = models.TextField(null=True)
    foods = models.TextField(null=True)


class Lifestyle(models.Model):
    gene_name = models.CharField(max_length=13)
    style=models.TextField(null=True)

#유저모델
class User(AbstractUser):
    nickname = models.CharField(max_length=20, unique=True, null=True,
                                validators=[validate_no_special_characters])
    
    def __str__(self):
        return self.email
    
    
    
    
    