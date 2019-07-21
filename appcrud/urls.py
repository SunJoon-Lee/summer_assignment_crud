from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('post/',views.post, name='post'),
    path('<int:appcrud_id>/',views.detail, name='detail'),
    path('home/',views.home, name='home'),
    path('<int:pk>/edit/', views.edit, name='edit'), 
    path('<int:pk>/delete/', views.delete, name='delete'), 
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]