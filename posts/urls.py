from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.PostList.as_view(), name="list"),
    path("create/", views.PostCreate.as_view(), name="create"),
    path("<slug:slug>/", views.PostDetail.as_view(), name="detail"),
    path("correct/<slug:slug>/", views.CorrectionCreate.as_view(), name="correct"),
    path(
        "correction/<slug:slug>/",
        views.CorrectionDetail.as_view(),
        name="correction_detail",
    ),
    path(
        "correction/list/<slug:post_slug>/",
        views.PostCorrectionList.as_view(),
        name="correction-list",
    ),
    path(
        "correction/mark-seen/<int:correction_id>/",
        views.confirm_author_viewed_correction,
        name="mark-correction-seen",
    ),
    path(
        "correction/validate/<int:correction_id>/",
        views.validate_correction,
        name="correction-validate",
    ),
]
