from django import forms

from .models import Blog


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['category', 'title', 'is_featured', 'image', 'content']

    def save(self, user=None):
        post = super(BlogPostForm, self).save(commit=False)
        if user:
            post.user = user
        post.save()
        return post
