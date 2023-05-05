from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mypage/', views.my_page, name='my_page'),
    path('daily_question/', views.daily_question, name='daily_question'),
    path('gene_register<int:property_id>/', views.gene_register, name='gene_register'),
    path('avartar_game/', views.avatar_game, name='avatar_game')
]
