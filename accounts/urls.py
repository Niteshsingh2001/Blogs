from django.urls import path
from . import views 

urlpatterns = [
    path('', views.signin),
    path('signout/', views.signout),
    path('reg/', views.reg),

]
