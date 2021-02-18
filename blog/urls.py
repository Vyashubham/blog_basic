from django.urls import path
from .views import PostListView, PostDetailView, BlogpostListView
# PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, ---> import removed from .views
from . import views
urlpatterns = [
    
    path('', PostListView.as_view(), name="website_home"),
    path('blog/', BlogpostListView.as_view(), name="blog_index"),
    path('post/<slug:slug>/', PostDetailView.as_view(), name="post_detail_view"),
    
]
