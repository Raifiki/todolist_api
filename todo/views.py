from django.shortcuts import render

from todo.models import Todo
from rest_framework import permissions, viewsets

from todo.serializers import TodoSerializer

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('created_at')
    serializer_class = TodoSerializer
    permission_classes = [] # kann auch leer sein  für eingeloggten user: permissions.IsAuthenticated
