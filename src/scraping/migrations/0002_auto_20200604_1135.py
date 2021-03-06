# Generated by Django 3.0.6 on 2020-06-04 06:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новости', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='news',
            name='timestamp',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='href_db',
            field=models.CharField(max_length=2048, unique=True, verbose_name='URL-адрес'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_image_db',
            field=models.ImageField(upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_preview_db',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title_db',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
    ]
