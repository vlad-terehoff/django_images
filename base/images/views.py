from django.shortcuts import render, reverse
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from images.forms import UserImagesForm, UserImagesUpdateForm
from images.models import UserImages, TagsImages
from django.urls import reverse_lazy


class Home(View):
    def get(self, request):
        return render(request, 'main/index.html')


class UserImagesListView(ListView):
    model = UserImages
    template_name = 'main/list_images.html'
    context_object_name = 'images'
    queryset = UserImages.objects.all().prefetch_related('tags')

    def get_queryset(self):
        queryset = super().get_queryset()

        name_filter = self.request.GET.get('name')
        shooting_date_filter = self.request.GET.get('shooting_date')
        tags_filter = self.request.GET.getlist('tags')

        if name_filter:
            queryset = queryset.filter(name__icontains=name_filter)
        if shooting_date_filter:
            queryset = queryset.filter(shooting_date=shooting_date_filter)
        if tags_filter:
            queryset = queryset.filter(tags__in=tags_filter).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = TagsImages.objects.all()
        return context


class UserImagesCreateView(CreateView):
    model = UserImages
    form_class = UserImagesForm
    template_name = 'main/create_image.html'
    success_url = reverse_lazy('list_images')

    def form_valid(self, form):
        user_image = form.save(commit=False)

        if user_image.image:
            user_image.image.name = form.cleaned_data['name']

        user_image.save()
        return super().form_valid(form)


class UserImagesDetailView(DetailView):
    model = UserImages
    template_name = 'main/image_detail.html'
    context_object_name = 'image'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        image = self.get_object()

        context['tags'] = image.tags.all()

        return context


class UserImagesUpdateView(UpdateView):
    model = UserImages
    form_class = UserImagesUpdateForm
    template_name = 'main/image_update.html'
    context_object_name = 'image'

    def get_success_url(self):

        return reverse('image_detail', kwargs={'pk': self.object.pk})


class UserImagesDeleteView(DeleteView):
    model = UserImages
    template_name = 'main/image_confirm_delete.html'
    context_object_name = 'image'
    success_url = reverse_lazy('list_images')
