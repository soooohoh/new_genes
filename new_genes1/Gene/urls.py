from django.urls import path
from . import views

urlpatterns = [
    #마이페이지
    path('', views.home, name='home'),
    path('mypage/', views.my_page, name='my_page'),
    path('mypage/properties/', views.property_confirm, name='property_confirm'),
    path('mypage/properties/gene_register/<int:property_id>', views.gene_register, name='gene_register'),
    path('mypage/properties/gene_register/<str:gene_name>', views.habits, name='habits'),


    # 데일리(설문조사)
    path('daily_question/', views.daily_question, name='daily_question'),
    #path('gene_register<int:property_id>/', views.gene_register, name='gene_register'),

    #아바타게임
    path('avartar_game/', views.avatar_game, name='avatar_game'),



    #프로필profile
    path('mypage/profile/<int:user_id>/', views.ProfileReadView.as_view(), name='profile'),
    path("set-profile/", views.ProfileSetView.as_view(), name="profile-set"),
    path('mypage/profile/<int:user_id>/edit/', views.ProfileUpdateView.as_view(), name='profile-update'),
]
