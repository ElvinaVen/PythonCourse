

from django.template.defaultfilters import slugify
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blogs.models import Blog

from blogs.services import get_articles_from_cache


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'image')
    success_url = reverse_lazy('blogs:list')


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = get_articles_from_cache()
        return queryset



class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body')
    success_url = reverse_lazy('blogs:list')

    def get_success_url(self):
        return reverse('blogs:view', kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs:list')
