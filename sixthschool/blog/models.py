from django.db import models
from django.urls import reverse


class Publications(models.Model):
    page_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, verbose_name='Идентификатор', db_index=True)
    image = models.ImageField(upload_to='photo/image/', blank=True, null=True)
    info = models.TextField(verbose_name='Описание', blank=True, null=True)
    category = models.CharField(max_length=20, verbose_name='Категория', default=None)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page', kwargs={'slug': self.slug})


class Options(models.Model):
    name = models.CharField(max_length=100, verbose_name='Опция')
    tag_open = models.TextField( verbose_name='Открывающий тег')
    tag_close = models.TextField(verbose_name='Закрывающий тег')
    npp = models.PositiveIntegerField(verbose_name="№", default=0)

    class Meta:
        verbose_name = "Опция"
        verbose_name_plural = "Опции"
        ordering = ('npp',)

    def __str__(self):
        return self.name

class Colors(models.Model):
    name = models.CharField(max_length=20, verbose_name='Цвет', unique=True)
    code = models.CharField(max_length=20, verbose_name='Код')

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"

    def __str__(self):
        return self.name



class ContentBlocks(models.Model):
    page = models.ForeignKey(Publications, related_name='content_blocks', on_delete=models.CASCADE, verbose_name='Страница')
    content = models.TextField(verbose_name='Текст', blank=True, null=True)  # Для текстовых блоков
    color = models.ForeignKey(Colors, verbose_name='Цвет', on_delete=models.CASCADE, default='Черный', blank=True, null=True)
    image = models.ImageField(upload_to='photo/image/', blank=True, null=True)  # Для изображений
    options = models.ManyToManyField(Options, blank=True, related_name='options')

    class Meta:
        verbose_name = "Блок"
        verbose_name_plural = "Блоки"
        ordering = ('id',)

    def get_option(self):
        return ", ".join([str(o) for o in self.options.all()])


    def __str__(self):
        return str(self.page)