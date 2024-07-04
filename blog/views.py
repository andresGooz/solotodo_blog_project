from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import ListCreateAPIView
from .models import Post
from .serializers import PostSerializer


class PostListView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class GetPostsView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def get_object(self):
        id = self.kwargs['id']
        return Post.objects.filter(pk=id).first()
