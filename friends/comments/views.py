from django.shortcuts import get_object_or_404, redirect, render
from .models import Comment
from posts.models import Post
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)

    return render(request, 'post_detail.html', {'post': post, 'form': form})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.author:
        comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

