from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Eating_Habits, Lifestyle
from Gene.models import Gene
# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Eating_Habits)
admin.site.register(Lifestyle)
admin.site.register(Gene)
UserAdmin.fieldsets += ('Custom fields', {'fields' : ('nickname',)}),
