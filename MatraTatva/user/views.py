from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def userregister(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created! You can login now.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/signup.html', {'form': form})