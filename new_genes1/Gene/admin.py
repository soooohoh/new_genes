from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Eating_Habits
from Gene.models import Gene
from Gene.models import LifeStyle
# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Eating_Habits)
admin.site.register(Gene)
admin.site.register(LifeStyle)
UserAdmin.fieldsets += ('Custom fields', {'fields' : ('nickname', 'intro', 'goals', 'profile_picture')}),
