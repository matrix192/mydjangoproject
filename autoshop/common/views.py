from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from buycars.models import Profile
from django.contrib.auth import login, logout

@login_required
def edit_profile(request):
    profile = Profile.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'registration/edit_profile.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'registration/profile.html', {'profile': request.user})

def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')
