from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.PostList.as_view(), name="list"),
    path("create/", views.PostCreate.as_view(), name="create"),
    path("<str:slug>/", views.PostDetail.as_view(), name="detail"),
    path("correct/<str:slug>/", views.TextCorrect.as_view(), name="correct"),
    path(
        "correction/<int:pk>/",
        views.TextCorrectionDetail.as_view(),
        name="correction_detail",
    ),
]
