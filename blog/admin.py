from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',  'created_at', 'author',)
    list_filter = ('author', 'created_at',)
    search_fields = ('title', 'content', 'author__username',)


admin.site.register(Post, PostAdmin)

