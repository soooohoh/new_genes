from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('gene_info/', views.gene_info, name='gene_info'),
    path('avatar_game/', views.avatar_game, name='avatar_game'),
    path('my_page/', views.my_page, name='my_page'),
    path('daily_question/', views.daily_question, name='daily_question'),
    path('gene_list/<int:property_id>', views.gene_list, name='gene_list'),
    path('gene_habit/<str:gene_name>', views.habits, name='gene_habit')
]
