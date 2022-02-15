from django.contrib import admin

from .models import (
    BlogCategory,
    Blog
    )


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'date_updated', 'timeStamp', 'is_featured']


admin.site.register(BlogCategory)
admin.site.register(Blog, BlogAdmin)
