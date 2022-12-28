from django.contrib import admin

# Register your models here.
from apps.forum.models import ForumModel, Post1, Comment


@admin.register(ForumModel)
class ForumAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('author', 'id', 'title')

@admin.register(Post1)
class ForumAdmin2(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'created_at', 'updated_at')

@admin.register(Comment)
class ForumAdmin2(admin.ModelAdmin):
    list_display = ('id', 'user', 'text', 'created_at', 'updated_at')
