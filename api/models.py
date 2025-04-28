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
    
class Commentaire :
    pass