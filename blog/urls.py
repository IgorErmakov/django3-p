from django.urls import path
from .views import BlogPostView, BlogPostDetailsView

app_name = 'blog'

urlpatterns = [
    path('', BlogPostView.as_view(), name = 'all_blogs'),
    path('<int:blog_id>.html', BlogPostDetailsView.as_view(), name = 'read-more'),
]
