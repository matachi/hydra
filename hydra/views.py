from django.views.generic import TemplateView, ListView
from blog.models import Post


class WelcomeView(ListView):
    template_name = 'hydra/welcome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'index'
        return context

    def get_queryset(self):
        return Post.objects.all().order_by('-date')[:5]


class AboutView(TemplateView):
    template_name = 'hydra/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'about'
        return context


class ContactView(TemplateView):
    template_name = 'hydra/online-presence.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'contact'
        return context
