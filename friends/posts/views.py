from django.shortcuts import redirect, render

from .forms import CreatePost
from .models import Post


def home_page(request):
    return render(request, "home.html")


def all_posts(request):
    template_name = "all_posts.html"
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, template_name, context)


def post_detail(request, post_id):
    template_name = "post_detail.html"
    post = Post.objects.get(id=post_id)
    context = {
        "post": post
    }
    return render(request, template_name, context)


def post_create(request):
    if request.method == 'POST':
        form = CreatePost(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:all_posts")
    else:
        form = CreatePost()

    return render(request, 'post_form.html', {'form': form})


def post_edit(request, post_id):
    post = Post.objects.get(id=post_id)
    form = CreatePost(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('posts:post_detail', post_id=post_id)
    return render(request, 'post_form.html', {'form': form})


def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect("posts:all_posts")
