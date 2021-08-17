from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views import View
from .models import Post

class BlogPostView(View):
    def get(self, request):

        items_per_page = 3

        page = int(request.GET.get('page', 1))

        # equals to DESC
        posts = Post.objects.order_by('-created_at')

        paginator = Paginator(posts, items_per_page)
        page      = paginator.get_page(page)
        # posts = []

        return render(
            request,
            'blog/all_blogs.html',
            {'page': page}
        )


class BlogPostDetailsView(View):
    def get(self, request, blog_id):

        post = get_object_or_404(Post, pk=blog_id)

        return render(
            request,
            'blog/detail.html',
            {'post': post}
        )
