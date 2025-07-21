from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CreatePost
from .models import Post


def home_page(request):
    posts = Post.objects.all().order_by("-created_at")
    paginator = Paginator(posts, 2)  # Show 5 posts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "home.html", {"page_obj": page_obj})


def all_posts(request):
    template_name = "all_posts.html"
    author_username = request.GET.get("author", "")
    posts = Post.objects.all()
    if author_username:
        posts = posts.filter(author__username__icontains=author_username)
    context = {
        "posts": posts,
        "author_filter": author_username
    }
    return render(request, template_name, context)


def post_detail(request, post_id):
    template_name = "post_detail.html"
    post = Post.objects.get(id=post_id)
    context = {
        "post": post
    }
    return render(request, template_name, context)


@login_required
def post_create(request):
    if request.method == 'POST':
        form = CreatePost(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:all_posts")
    else:
        form = CreatePost()

    return render(request, 'post_form.html', {'form': form})


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CreatePost(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('posts:post_detail', post_id=post_id)
    return render(request, 'post_form.html', {'form': form})


@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect("posts:all_posts")
