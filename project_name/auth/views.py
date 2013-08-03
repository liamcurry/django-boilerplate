from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login as signin, logout
from django.shortcuts import redirect, render


__all__ = ['join', 'signin', 'logout']


def join(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST, prefix='join')
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = UserCreationForm(prefix='join')
    return render(request, 'auth/join.html', {'form': form})
