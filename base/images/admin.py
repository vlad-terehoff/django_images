from django.contrib import admin
from images.models import UserImages, TagsImages


admin.site.register([UserImages, TagsImages])
