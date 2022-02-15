from django.views import generic
from django.urls import reverse_lazy

from .models import (
        BlogCategory,
        Blog
    )

from .forms import BlogPostForm


class BlogPostView(generic.CreateView):
    form_class = BlogPostForm
    success_url = reverse_lazy('blog')
    template_name = 'updates/blog_post.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class BlogListPageView(generic.ListView):
    model = Blog
    context_object_name = 'posts'
    paginate_by = 12
    template_name = 'updates/blog.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogListPageView, self).get_context_data(*args, **kwargs)
        context['categories'] = BlogCategory.objects.all()
        return context


class BlogDetailPageView(generic.DetailView):
    model = Blog
    context_object_name = 'detail'
    template_name = 'updates/blog_detail.html'

    def context_data(self, *args, **kwargs):
        post = self.object.category
        context = super(BlogDetailPageView, self).get_context_data(*args, **kwargs)
        context['post_detail'] = Blog.objects.filter(category__name=post)
        return context
