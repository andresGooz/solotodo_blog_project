from django.urls import path
from . import views
from django.urls import path
from .views import GetPostsView, PostListView


urlpatterns = [
    path('api/posts/', PostListView.as_view(), name='get_post_posts'),
    path('api/posts/<str:id>/', GetPostsView.as_view(), name='get_posts_by_id'),
]