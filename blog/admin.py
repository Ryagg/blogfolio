from django.contrib import admin
from django.utils.html import format_html

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'content', 'created_on')
    list_editable = ('content',)
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    def content_view(self, obj):
        return format_html('{}', obj.content)


admin.site.register(Post, PostAdmin)
