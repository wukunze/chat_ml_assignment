from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render


def sign_up(request):
    """Processes the GET request to render the "Sign Up" page.
    If the request is a POST request, validates, logs the User in
    and redirects to the index page.

    Args:
        request: the request.

    return:
        The response that contains the index page or the "Sign Up" page.
    """
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, "ubs_project/index.html")
    context['form'] = form
    return render(request, "ubs_project/sign_up.html", context)