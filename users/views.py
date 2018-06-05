from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import UserChangeForm

def register(request):
    if request.user.is_authenticated:
        return redirect('list_notes')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('list_notes')
    else:
        form = UserCreationForm()

    return render(request, 'registration/registration.html', {'form': form})

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')

    user = User.objects.get(pk=request.user.id)

    form = UserChangeForm(request.POST or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect('profile')

    return render(request, 'registration/profile.html', {'form': form})