from django.contrib import admin
from django.contrib.admin.decorators import register
from . import models

# Register your models here.
@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',),}

admin.site.register(models.Category)