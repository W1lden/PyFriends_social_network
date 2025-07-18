from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model

from .forms import UserProfileForm
from .models import UserProfile

User = get_user_model()


@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(UserProfile, user=user)
    return render(request, "profiles/profile.html", {"profile": profile})

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
