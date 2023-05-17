from django.urls import path
from . import views

urlpatterns = [
    #마이페이지
    path('', views.home, name='home'),
    path('mypage/', views.my_page, name='my_page'),
    path('mypage/properties/', views.property_confirm, name='property_confirm'),
    path('mypage/properties/gene_info/<int:property_id>', views.gene_info, name='gene_info'),
    path('mypage/properties/gene_info/habits/<str:gene_name>', views.habits, name='habits'),


    # 데일리(설문조사)
    path('daily_question/', views.daily_question, name='daily_question'),
    #path('gene_register<int:property_id>/', views.gene_register, name='gene_register'),

    #아바타게임
    path('avartar_game/', views.avatar_game, name='avatar_game'),

    #유전일기
    path('gene_diary_list/<int:user_id>', views.Gene_Diary_List_View.as_view(), name='gene_diary_list'),
    
    
    #프로필profile
    path('mypage/profile/<int:user_id>/', views.ProfileReadView.as_view(), name='profile'),
    path("set-profile/", views.ProfileSetView.as_view(), name="profile-set"),
    #path('mypage/profile/<int:user_id>/edit/', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('mypage/profile/<int:user_id>/edit/', views.ProfileUpdateView, name='profile-update'),
]
