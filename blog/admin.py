from django.contrib import admin
from .models import Post, RePost

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'published_date', 'author')

class RePostAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'published_date', 'author', 'post')

admin.site.register(Post, PostAdmin)
admin.site.register(RePost, RePostAdmin)

