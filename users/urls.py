from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path(
        "unshow-notifications/",
        views.unshow_notifications,
        name="unshow-notifications",
    ),
    path("<str:username>/posts/", views.UserPostList.as_view(), name="posts"),
    path(
        "<str:username>/corrections/",
        views.UserCorrectionsList.as_view(),
        name="corrections",
    ),
    path(
        "<str:username>/corrected/",
        views.UserCorrectedList.as_view(),
        name="corrected",
    ),
]
