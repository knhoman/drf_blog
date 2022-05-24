from django.shortcuts import render

from rest_framework import viewsets
from .serilizers import PostSerializer
from .models import Post
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
	serilizer_class = PostSerializer
	queryset = Post.objects.all()
	loolup_field = "slug"
