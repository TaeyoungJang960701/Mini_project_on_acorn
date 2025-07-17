from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('home/', views.members, name='members'),
    path('detail/', views.details, name='detail'),
]

# path('detail/<int:member_id>/', views.detail, name='detail'),