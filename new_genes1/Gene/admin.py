from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Eating_Habits
from Gene.models import Gene
from Gene.models import LifeStyle
from Gene.models import Diary
# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Eating_Habits)
admin.site.register(Gene)
admin.site.register(LifeStyle)
admin.site.register(Diary)
UserAdmin.fieldsets += ('Custom fields', {'fields' : ('nickname', 'intro', 'goals', 'profile_picture', 'FTO_gene', 'MC4R_gene', 'BDNF_gene')}),
