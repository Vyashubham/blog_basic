from django.urls import path
from blog import views
from .views import PostListView, PostDetailView, BlogpostListView
urlpatterns = [
    path('', PostListView.as_view(), name="website_home"),
    path('profile/', views.profile, name='profile'),
    path('blog/', BlogpostListView.as_view(), name="blog_home"),
    path('post/<slug:slug>/', PostDetailView.as_view(), name="post_detail_view"),
]
 
    
    
    
    