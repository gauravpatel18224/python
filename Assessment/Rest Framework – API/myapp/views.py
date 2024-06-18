from django.shortcuts import render
from rest_framework import generics
from .models import Comment
from .serializers import Commenterializer
# Create your views here.


class CommentList(generics.ListCreateAPIView):
	queryset=Comment.objects.all()
	serializer_class=CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=Comment
	serializer_class=CommentSerializer