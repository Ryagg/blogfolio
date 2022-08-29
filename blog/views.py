from django.views import generic

from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

    def get_queryset(self):
        return self.queryset.all()


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
