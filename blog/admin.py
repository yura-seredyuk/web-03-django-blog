from blog.models import Post
from django.utils.safestring import mark_safe
from django.contrib import admin


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('image_show', 'title', 'author', 'create_date' ,'publish_date')
    list_filter = ('author', 'create_date' ,'publish_date')
    search_fields = ('title', 'text')
    date_hierarchy = 'publish_date'
    ordering = ['author', 'publish_date']

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"

    image_show.__name__ = 'images'

admin.site.register(Post, PostAdmin)