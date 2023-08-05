from django.urls import path
from .views import PostView, getPost, getPostsByTag, about

urlpatterns = [
    path('', PostView, name='home'),
    path('detail/<int:pk>/', getPost, name='post_detail'),
    path('filter/<str:tagName>/', getPostsByTag, name='post_filter'),
    path('about/', about, name='about_me')
]
