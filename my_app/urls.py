from django.urls import path
from . import views
from .views import (
    Home,
    upload,
)

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),
]