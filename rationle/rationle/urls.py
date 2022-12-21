"""rationle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rating.views import SimpleView, SimpleFormView
from django.contrib import admin
from django.urls import path
from rating.views import RatingsListView, RatingsEntryListView, RatingsDetailView

from registration.views import RegistrationView, LoginiView, ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',RatingsListView.as_view(), name="main" ),
    path('form/',SimpleFormView.as_view() ),
    path('entry/<name>/',RatingsEntryListView.as_view() ),
    path('rating/<int:pk>/',RatingsDetailView.as_view() ),
    path('register/',RegistrationView.as_view() ),
    path('login/',LoginiView.as_view(), name="login"),
    path('accounts/profile/', ProfileView.as_view())
]
