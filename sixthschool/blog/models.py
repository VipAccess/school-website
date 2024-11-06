# from django.db import models
#
# class Publications(models.Model):
#     title = models.CharField(max_length=200)
#     slug = models.SlugField(unique=True)
#     type = models.CharField(max_length=20)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_published = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.title
#
# class ContentBlock(models.Model):
#     PAGE_BLOCK_TYPES = [
#         ('text', 'Text'),
#         ('image', 'Image'),
#         ('video', 'Video'),
#     ]
#
#     page = models.ForeignKey(Publications, related_name='content_blocks', on_delete=models.CASCADE)
#     block_type = models.CharField(max_length=10, choices=PAGE_BLOCK_TYPES)
#     content = models.TextField(blank=True)  # Для текстовых блоков
#     image = models.ImageField(upload_to='photo/image/', blank=True, null=True)  # Для изображений
#     video_url = models.URLField(blank=True, null=True)  # Для видео
#
#     def __str__(self):
#         return f"{self.get_block_type_display()} Block for {self.page.title}"