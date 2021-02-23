"""cse_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from django.conf.urls import url
from django.shortcuts import render, HttpResponse
from ubs_project import views

def registration(request):
    return render(request, 'registration_page.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('ubs_project/', include('ubs_project.urls'))
    path('register/', views.registrationPage),
    path('register/student', views.registrationStudent),
    path('login/', views.loginPage)
]

# Add URL maps to redirect the base URL to our application
urlpatterns += [
    #path('', RedirectView.as_view(url = 'ubs_project/', permanent = True))
]
