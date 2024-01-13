from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    # здесь можно настроить отображение модели
    list_display = ['title', 'date_posted', 'author']

