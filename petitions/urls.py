from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='petitions.index'),
    path('like/', views.like_petition, name='petitions.like'),
]