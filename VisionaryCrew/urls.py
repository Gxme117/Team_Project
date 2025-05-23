"""
URL configuration for VisionaryCrew project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from myapp.views import landing, about, team, demo, feedback_view, thank_you

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),      # Landing page is the root URL
    path('about/', about, name='about'),
    path('team/', team, name='team'),
    path('demo/', demo, name='demo'),
    path('feedback/', feedback_view, name='feedback'),
    path('thank-you/', thank_you, name='thank_you'),
]


