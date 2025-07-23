from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseForbidden

from posts.models import Post
from profiles.forms import UserProfileForm
from profiles.models import UserProfile

User = get_user_model()


@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(UserProfile, user=user)
    posts = Post.objects.filter(author=user).order_by("-created_at")
    is_own_profile = request.user == user
    return render(request, "profile_view.html", {
        "profile": profile,
        "posts": posts,
        "is_own_profile": is_own_profile
    })


@login_required
def profile_edit(request, username):
    if request.user.username != username and not request.user.is_superuser:
        return HttpResponseForbidden(
            "Вы не можете редактировать чужой профиль."
        )

    profile = get_object_or_404(UserProfile, user__username=username)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profiles:profile", username=username)
    else:
        form = UserProfileForm(instance=profile)

    return render(request, "profile_edit.html", {"form": form})
