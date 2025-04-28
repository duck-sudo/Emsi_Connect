from django.db import models
from django.utils import timezone
# Create your models here.


class Posts(models.Model):
    name = models.CharField(max_length=22) #change name to user info with class user
    date_creation = models.DateField(default=timezone.now)
    date_modification = models.DateField(default=timezone.now)
    contenu_texte = models.CharField(max_length=200,default="empty")
    media = models.ImageField(null=True)

    def __str__(self):
        return self.name
    
    def num_comments(self):
        return self.comments.count()

    def num_likes(self):
        return self.likes.count()
    
class Commentaire(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments', null=True)
    author_name = models.CharField(max_length=100)  # badal hadi l class user type
    content = models.TextField()  
    
    
    def __str__(self):
        return f"Comment by {self.author_name} on {self.post.name}"




class Likes(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='likes', null=True)
    user_name = models.CharField(max_length=100,default="Anonymous") 


    def __str__(self):
        return f"Like by {self.user_name} on {self.post.name}"