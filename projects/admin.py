from django.contrib import admin
from projects.models import Platform, ProgrammingLanguage, Library, Tool, \
    Screenshot, Project, Link


admin.site.register(Platform)
admin.site.register(ProgrammingLanguage)
admin.site.register(Library)
admin.site.register(Tool)
admin.site.register(Screenshot)
admin.site.register(Link)


class LinkInline(admin.StackedInline):
    model = Link


class ProjectAdmin(admin.ModelAdmin):
    inlines = [LinkInline]


admin.site.register(Project, ProjectAdmin)
