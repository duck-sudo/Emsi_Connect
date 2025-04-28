from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework import status 
from .models import Posts
from .serializer import PostsSerializer
from datetime import date

# Create your views here.

@api_view(['GET'])
def get_posts(request):
    all_posts = Posts.objects.all()  
    serializer = PostsSerializer(all_posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_posts(request):
    serializer = PostsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def posts_detail(request, pk):
    try:
        post = Posts.objects.get(pk=pk)
    except Posts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostsSerializer(post)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PostsSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
