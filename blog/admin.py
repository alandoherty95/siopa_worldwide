from django.contrib import admin
from .models import BlogPost


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(BlogPost, BlogAdmin)
