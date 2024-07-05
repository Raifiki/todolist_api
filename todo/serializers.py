from django.contrib.auth.models import User
from rest_framework import serializers

from todo.models import Todo 

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','username','email']

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Todo
        fields = ['id','created_at','title','description','user','myFunction']