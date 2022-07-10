
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home),
    path('article/<int:article_id>/', views.article),
    path('articles/', views.search),
    path('articles/create/', views.create),
    path('articles/created/', views.created),
]
