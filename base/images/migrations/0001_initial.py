# Generated by Django 5.1.5 on 2025-01-30 15:21

import images.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TagsImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название тега')),
            ],
            options={
                'verbose_name': 'Тэг изображения',
                'verbose_name_plural': 'Тэги изображений',
            },
        ),
        migrations.CreateModel(
            name='UserImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название изображения')),
                ('description', models.TextField(verbose_name='Описание изображения')),
                ('shooting_date', models.DateField(verbose_name='Дата съёмки изображения')),
                ('image', models.ImageField(upload_to=images.models.images_directory_path, verbose_name='Изображение')),
                ('tags', models.ManyToManyField(blank=True, related_name='user_images', to='images.tagsimages', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Изображение пользователя',
                'verbose_name_plural': 'Изображения пользователя',
            },
        ),
    ]
