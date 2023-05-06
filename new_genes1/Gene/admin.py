from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Eating_Habits, Lifestyle
# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Eating_Habits)
admin.site.register(Lifestyle)
UserAdmin.fieldsets += ('Custom fields', {'fields' : ('nickname',)}),
