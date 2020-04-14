"""BookOmatic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include, path
from django.contrib import admin


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.HomePage.as_view(), name="home"),
    url(r"^accounts/", include("allauth.urls")),
    url(r"", include("calendarapp.urls")),
    url(r"^admin/", admin.site.urls),
]

# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("accounts/", include("django.contrib.auth.urls")),
]
