from django.views.generic import ListView
from projects.models import Project


class ProjectsView(ListView):
    template_name = 'projects/list.html'
    queryset = Project.objects.order_by('-order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'projects'
        return context
