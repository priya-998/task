from django.urls import path,include
from . import views


urlpatterns = [
    path('index/', views.index, name="index"),
    path('details', views.details, name="details"),
    path('changepassword', views.changepassword, name="changepassword"),
    path('home', views.home, name="home"),
    path('gallery', views.gallery, name="gallery"),
    path('login', views.login, name="login"),
    path('registration/', views.registration, name="registration"),
    path('update', views.update, name="update"),
]

