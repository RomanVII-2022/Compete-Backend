from django.shortcuts import render
from myapp.models import Category, Blog
from myapp.serializers import CategorySerializer, BlogSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'id'


    @action(detail=False)
    def getRecent(self, request):
        blogs = Blog.objects.all().order_by('-id')[:3]
        serializer = self.get_serializer(blogs, many=True)
        return Response(serializer.data)


class BlogCategoryViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Blog.objects.filter(category=pk)
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)


    