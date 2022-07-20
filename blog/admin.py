from django.contrib import admin
from blog.models import Post

# Register your models here.
@admin.register(Post)
class AdminPostsList(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date_pub')
    prepopulated_fields = {"slug": ("title",)}