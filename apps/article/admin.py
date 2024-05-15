from django.contrib import admin
from .models import Category, Comment, Tag, Article

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Article)
