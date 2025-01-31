from django.urls import path
from .views import (Home, UserImagesListView, UserImagesCreateView,
                    UserImagesDetailView, UserImagesUpdateView, UserImagesDeleteView)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('list_images', UserImagesListView.as_view(), name='list_images'),
    path('create_image', UserImagesCreateView.as_view(), name='create_image'),
    path('image_detail/<int:pk>/', UserImagesDetailView.as_view(), name='image_detail'),
    path('image_update/<int:pk>/', UserImagesUpdateView.as_view(), name='image_update'),
    path('image_delete/<int:pk>/', UserImagesDeleteView.as_view(), name='image_delete'),
]