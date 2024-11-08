from django.contrib import admin
from .models import Publications, Options, BlockTypes, ContentBlocks, Colors

@admin.register(Publications)
class PublicationsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'info', 'category', 'created_at', 'updated_at', 'is_published']

@admin.register(Options)
class OptionsAdmin(admin.ModelAdmin):
    list_display = ['name', 'tag_open', 'tag_close']

@admin.register(BlockTypes)
class BlockTypesAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(ContentBlocks)
class ContentBlocksAdmin(admin.ModelAdmin):
    list_display = ['page', 'block_type', 'content', 'color', 'image', 'url', 'npp', 'get_option']

@admin.register(Colors)
class ColorsAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']
