from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse

from blog.models import Blogs


class BlogsCreateView(CreateView):
    model = Blogs
    fields = ['title', 'note', 'image', 'views_count']
    template_name = 'blog/blogs_form.html'
    success_url = reverse_lazy('blog:list')


class BlogsListView(ListView):
    model = Blogs

    def get_queryset(self):
        return Blogs.objects.filter(is_published=True)


class BlogsUpdateView(UpdateView):
    model = Blogs
    fields = ['title', 'note', 'image', 'views_count']
    template_name = 'blog/blogs_form.html'
    success_url = reverse_lazy('blog:list')

    def get_success_url(self):
        return reverse('blog:detail', args=[self.kwargs.get('pk')])


class BlogsDeleteView(DeleteView):
    model = Blogs
    success_url = reverse_lazy('blog:list')


class BlogsDetailView(DetailView):
    model = Blogs

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count +=1
        self.object.save()
        return self.object
