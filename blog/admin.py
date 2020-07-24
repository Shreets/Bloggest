from django.contrib import admin
from blog.models import Blog


class BlogAdmin(admin.ModelAdmin):
    readonly_fields = 'date_created',


# Register your models here.
admin.site.register(Blog, BlogAdmin)