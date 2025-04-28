from rest_framework import serializers
from .models import Posts, Commentaire, Likes

class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = ['author_name', 'content']

class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = ['user_name']

class PostsSerializer(serializers.ModelSerializer):
    num_comments = serializers.SerializerMethodField()
    num_likes = serializers.SerializerMethodField()

    class Meta:
        model = Posts
        fields = ['id', 'name', 'date_creation', 'date_modification', 'contenu_texte', 'media', 'num_comments', 'num_likes']

    def get_num_comments(self, obj):
        return obj.comments.count()

    def get_num_likes(self, obj):
        return obj.likes.count()
