from django.db import models


# Create your models here.
class News(models.Model):
    title_db = models.CharField(max_length=255, verbose_name='Заголовок')
    href_db = models.CharField(max_length=2048, verbose_name='URL-адрес', unique=True)
    news_preview_db = models.TextField(verbose_name='Текст')
    news_image_db = models.CharField(max_length=2048, verbose_name='URL-адрес изображения', unique=True)
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='Новости'
        verbose_name_plural='Новости'
        
    def __str__(self):
        return self.title_db
