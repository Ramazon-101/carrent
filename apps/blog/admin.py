from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')
    search_fields = ['title', ]
    list_display_links = ('title', 'id')
    list_per_page = 50
    search_help_text = 'search on here'


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ['title', ]
    list_filter = ('id', 'title')
    list_display_links = ('title', 'id')
    search_help_text = 'search on here'


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ['title', 'category__title']
    list_filter = ('category', 'tag')
    list_display_links = ('title', 'id')
    filter_horizontal = ('tag',)
    search_help_text = 'search on here'
    date_hierarchy = 'created_at'


admin.site.register(Blog, BlogAdmin)
admin.site.register(About)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(History)
admin.site.register(How_it_works)
admin.site.register(Our_Team)