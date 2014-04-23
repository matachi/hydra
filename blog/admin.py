from django.contrib import admin
from blog.models import Post, Tag


class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tag, TagAdmin)


class TagInline(admin.TabularInline):
    model = Post.tags.through
    extra = 1


def resave(modeladmin, request, queryset):
    for post in queryset:
        post.save()
resave.short_description = 'Update selected posts\' HTML and slug'


class PostAdmin(admin.ModelAdmin):
    # inlines = TagInline,
    readonly_fields = 'content_html', 'slug'
    actions = [resave]

admin.site.register(Post, PostAdmin)

