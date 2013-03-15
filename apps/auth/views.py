from django.conf import settings
from django.contrib.auth import (login as auth_login, logout as auth_logout,
                                 REDIRECT_FIELD_NAME)
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.shortcuts import render, redirect, resolve_url
from django.utils.http import is_safe_url


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = UserCreationForm()

    return render(request, 'auth/signup.html', {'form': form})


@sensitive_post_parameters()
@never_cache
def login(request):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.REQUEST.get(REDIRECT_FIELD_NAME, '')

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            user = form.get_user()

            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(user.get_absolute_url())

            # Okay, security check complete. Log the user in.
            auth_login(request, user)

            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()

            return redirect(redirect_to)
    else:
        form = AuthenticationForm(request)

    request.session.set_test_cookie()

    return render(request, 'auth/login.html', {'form': form})


def logout(request, next_page=None):
    """
    Logs out the user and displays 'You are logged out' message.
    """
    auth_logout(request)

    if REDIRECT_FIELD_NAME in request.REQUEST:
        next_page = request.REQUEST[REDIRECT_FIELD_NAME]
        # Security check -- don't allow redirection to a different host.
        if not is_safe_url(url=next_page, host=request.get_host()):
            next_page = request.path

    if next_page:
        # Redirect to this page until the session has been cleared.
        return redirect(next_page)

    return redirect('/')
