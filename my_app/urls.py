from django.urls import path
from . import views
from .views import (
    Home,
    upload,
    book_list,
    upload_book,
)

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),
    path('books/', views.book_list, name='book_list'),
    path('books/upload', views.upload_book, name='upload_book'),
]