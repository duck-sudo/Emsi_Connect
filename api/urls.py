from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', views.get_posts, name='get_posts'),  
    path('posts/create/', views.create_posts, name='create_posts'),  
    path('posts/<int:pk>/', views.posts_detail, name='posts_detail'),  
]