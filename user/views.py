from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignupForm

def index(request):
    return render(request, 'user/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('reminder:index')
    else:
        form = SignupForm()
    return render(request, 'user/signup.html', {'form': form})