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
    path('user_login/book_list/', views.book_details, name='book_list'),
    path('user_login/borrowed_book/', views.user_borrowed, name='borrowed_book'),
    path('user_login/edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('user_login/book_list<int:id>/', views.delete_item, name='book_list'),
]