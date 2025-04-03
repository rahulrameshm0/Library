from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_login/signup/', views.signup, name='signup'),
    path('user_login/logout/', views.user_logout, name='logout'),
    path('user_login/library/', views.library, name='library'),
    path('user_login/add_author/', views.add_author, name='add_author'),
    path('user_login/add_book/', views.add_book, name='add_book'),
]
