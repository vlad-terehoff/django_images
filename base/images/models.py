from django.db import models


class TagsImages(models.Model):
    class Meta:
        verbose_name = 'Тэг изображения'
        verbose_name_plural = 'Тэги изображений'

    name = models.CharField(max_length=50, unique=True, verbose_name="Название тега")

    def __str__(self) -> str:
        return self.name


def images_directory_path(instance, filename):
    return f'image_{instance.name}/{filename}'


class UserImages(models.Model):
    class Meta:
        verbose_name = 'Изображение пользователя'
        verbose_name_plural = 'Изображения пользователя'

    name = models.CharField(max_length=255, verbose_name="Название изображения")
    description = models.TextField(verbose_name="Описание изображения")
    shooting_date = models.DateField(verbose_name="Дата съёмки изображения")
    image = models.ImageField(verbose_name="Изображение", upload_to=images_directory_path)
    tags = models.ManyToManyField(TagsImages, blank=True, related_name='user_images', verbose_name="Теги")

    def __str__(self) -> str:
        return self.name
