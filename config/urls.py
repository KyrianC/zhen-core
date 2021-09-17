"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from custom_auth.views import CustomLoginView

urlpatterns = [
    path("admin/", admin.site.urls),
    # put before dj_rest_auth.urls to prioritize it over dj_rest_auth api/auth/login/ view
    path("api/auth/login/", CustomLoginView.as_view(), name="custom-login"),
    path("api/auth/", include("dj_rest_auth.urls")),
    path("api/posts/", include("posts.urls")),
    path("api/users/", include("users.urls")),
    # path("verify-email/", VerifyEmailView.as_view(), name="rest_verify_email"),
    path(
        "api/auth/registration/account-confirm-email/",
        VerifyEmailView.as_view(),
        name="account_email_verification_sent",
    ),
    path(
        "api/auth/registration/account-confirm-email/<str:key>/",
        ConfirmEmailView.as_view(),
    ),
    path("api/auth/registration/", include("dj_rest_auth.registration.urls")),
]
