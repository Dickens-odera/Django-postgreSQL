from django.shortcuts import render
#from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import PostsSerializer
from .models import Posts

# Create your views here.
class PostsView(viewsets.ModelViewSet):
    queryset = Posts.objects.all()  #query the table to get a alist of all the objects 
    #lookup_field = 'pk'
    serializer_class = PostsSerializer
    
    def get_queryset(self):
        return Posts.objects.all()

    
    


