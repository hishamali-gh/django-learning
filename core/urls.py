from django.urls import path

from . import views

urlpatterns = [
    path('', views.greet, name='greet'),
    path('user/<str:username>/', views.user_profile, name='profile')
]
