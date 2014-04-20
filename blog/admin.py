from django.contrib import admin
from blog.models import Post, Tag


class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tag, TagAdmin)


class TagInline(admin.TabularInline):
    model = Post.tags.through
    extra = 1


class PostAdmin(admin.ModelAdmin):
    # inlines = TagInline,
    readonly_fields = 'content_html', 'slug'

admin.site.register(Post, PostAdmin)

