from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from posts.models import Post

from .forms import CommentForm
from .models import Comment


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        # print("Ошибки формы:", form.errors)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('posts:post_detail', post_id=comment.post.pk)

    return render(request, 'post_detail.html', {'post': post, 'form': form})


@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    if request.user == comment.author:
        comment.delete()
    return redirect('posts:post_detail', post_id=comment.post.pk)
