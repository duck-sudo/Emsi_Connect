from django.urls import path
from .views import get_posts,create_posts,posts_detail

urlpatterns = [
    path('posts/', get_posts , name ='get_posts'),
    path('posts/create/', create_posts , name ='create_posts'),
    path('posts/<int:pk>', posts_detail ,name='posts_detail' )
]