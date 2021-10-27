from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("<str:username>/posts/", views.UserPostList.as_view(), name="posts"),
    path(
        "<str:username>/corrections/",
        views.UserCorrectionsList.as_view(),
        name="corrections",
    ),
]
