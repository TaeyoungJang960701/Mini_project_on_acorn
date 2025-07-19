from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView , name='home'),
    path('login/', views.LoginView , name='login'),
	path('signup/', views.SignupView , name='signup'),
    path('members/', views.MembersView, name='members'),
    path('members/<int:user_id>/', views.MembersDetailView, name='member_detail'),
    path('members/me', views.MeView, name='mypage'),
]