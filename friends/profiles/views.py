from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import UserProfileForm
from .models import UserProfile
from .posts.models import Post

User = get_user_model()


@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(UserProfile, user=user)
    posts = Post.objects.filter(author=user).order_by("-created_at")
    is_own_profile = request.user == user
    return render(request, "profiles/profile.html", {
        "profile": profile,
        "posts": posts,
        "is_own_profile": is_own_profile
    })


@login_required
def edit_profile(request):
    profile = request.user.userprofile

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profiles:profile", username=request.user.username)
    else:
        form = UserProfileForm(instance=profile)

    return render(request, "profiles/edit_profile.html", {"form": form})
