from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostsSerializer
from .models import Posts
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class PostsView(viewsets.ModelViewSet):
    queryset = Posts.objects.all()  #query the table to get a alist of all the objects 
    #lookup_field = 'pk'
    serializer_class = PostsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes =  (IsAuthenticated,)
    

    '''
    def get_queryset(self):
        return Posts.objects.all()
'''

    



    


