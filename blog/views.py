from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView

from blog.models import Post


class PostsView(ListView):
    template_name = 'blog/posts.html'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'blog'
        return context


class PostView(DetailView):
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'blog'
        return context

    def get_object(self):
        print(self.kwargs['slug'])
        post = Post.objects.get(slug=self.kwargs['slug'])
        if post.date.year == int(self.kwargs['year']) and \
           post.date.month == int(self.kwargs['month']) and \
           post.date.day == int(self.kwargs['day']):
            return post
        else:
            raise Http404(post.get_absolute_url())

    def get(self, request, *args, **kwargs):
        try:
            return super().get(self, request, *args, **kwargs)
        except Http404 as e:
            return redirect(e.args[0])
