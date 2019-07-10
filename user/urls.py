from django.urls import path, include
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('login/', views.loginView, name='loginView'),
    path('logout/', views.logoutView, name='logoutView'),
    path('register/', views.registerView, name='registerView'),
    path('user_center/', views.user_center, name='user_center'),
    path('user_center/edit_profile', views.edit_profile, name='edit_profile'),
    path('user_center/change_password', views.change_password, name='change_password'),

]
