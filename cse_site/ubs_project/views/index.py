from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    """Processes the GET request to render the index page.

    Args:
        request: the request object.

    Returns:
        The response that contains the index page.
    """
    return render(request, "ubs_project/index.html")