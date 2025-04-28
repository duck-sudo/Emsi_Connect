from rest_framework import serializers 
from .models import Posts

class postsSerializer(serializers.ModelSerializer):
    class Meta :
        model = Posts
        fields = '__all__' # 3 stooro lakhrin ki 3awnok transformi data l json