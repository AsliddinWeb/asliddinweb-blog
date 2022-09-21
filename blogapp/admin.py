from django.contrib import admin
from .models import Blog_Post

class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}

# Register your models here.
admin.site.register(Blog_Post, BlogPostAdmin)