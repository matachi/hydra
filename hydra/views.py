from django.views.generic import TemplateView


class Main(TemplateView):
    template_name = 'base.html'


class Contact(TemplateView):
    template_name = 'hydra/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'contact'
        return context
