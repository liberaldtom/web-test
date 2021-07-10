from django.contrib import admin
from .models import Category, Post
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published')
    ordering = ('author', 'published')
    search_fields = ['content']
    date_hierarchy = 'published'
    list_filter = ('author__username','categories__name')
        

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)