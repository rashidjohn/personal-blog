from django.contrib import admin
from .models import Post, Comment, Tag, About
from django.contrib.auth.models import Group
# Register your models here.

admin.site.unregister(Group)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommnetAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass