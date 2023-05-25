from django.urls import path
from . import views

urlpatterns = [
    #홈
    path('', views.home, name='home'),


    #유전자 정보
    path('properties/', views.property_confirm, name='properties'),
    path('properties/gene_info/<int:property_id>', views.gene_info, name='gene_info'),
    path('properties/gene_info/habits/<str:gene_name>', views.habits, name='habits'),


    # 데일리(설문조사)
    path('daily_question/', views.daily_question, name='daily_question'),
    #path('gene_register<int:property_id>/', views.gene_register, name='gene_register'),

    #아바타게임
    path('avartar_game/', views.avatar_game, name='avatar_game'),

    #유전일기
    path('gene_diary_list/<int:user_id>', views.Gene_Diary_List_View.as_view(), name='gene_diary_list'),
    path('gene_diary_list/gene_diary_detail_view/<int:diary_id>/', views.Gene_Diary_Detail_View.as_view(), name='gene_diary_detail'),
    path('gene_diary_list/gene_diary_create/', views.Gene_Diary_Create_View.as_view(), name='gene_diary_create'),
    path('gene_diary_list/gene_diary_detail_view/<int:diary_id>/edit', views.Gene_Diary_Update_View.as_view(), name="gene_diary_update"),
    path('gene_diary_list/gene_diary_detail_view/<int:diary_id>/delete', views.Gene_Diary_Delete_View.as_view(), name="gene_diary_delete"),


    #프로필profile
    path('profile/<int:user_id>/', views.ProfileReadView.as_view(), name='profile'),
    path("set-profile/", views.ProfileSetView.as_view(), name="profile-set"),
    path('edit-profile/', views.ProfileUpdateView.as_view(), name="profile-update"),

    #유전자 등록/확인
    path('mypage/properties/property_detail/<int:property_id>', views.property_detail, name='property_detail'),
    path('mypage/properties/gene_confirm/<int:user_id>', views.gene_confirm, name='gene_confirm'),
    path('mypage/properties/gene_register/<int:user_id>', views.gene_register, name='gene_register'),
]
