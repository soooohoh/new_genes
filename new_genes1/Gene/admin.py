from django.contrib import admin
from .models import Gene
from .models import Property
# Register your models here.
admin.site.register(Gene)
admin.site.register(Property)