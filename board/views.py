from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class PostListView(ListView):
    model = Post
    template_name = 'board/posts.html'
    context_object_name = 'post_list'
    paginate_by = 20

    def get_queryset(self):
        return Post.objects.order_by('-created_date')

class PostDetailView(DetailView):
    model = Post
    template_name = 'board/detail.html'
    context_object_name = 'post'

class CreatePostView(CreateView):
    model = Post

class UpdatePostView(UpdateView):
    return render()

class DeletePostView(DeleteView):


    
