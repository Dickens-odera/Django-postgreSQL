from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers #takes care of generating all the urls
from . import views
#create a router instance
router = routers.DefaultRouter()
router.register('api/posts',views.PostsView)

urlpatterns = [
     #path('posts',views.index, name="index"),
     url('',include(router.urls))
]

