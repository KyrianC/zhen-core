from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.PostList.as_view(), name="list"),
    path("<slug:slug>/", views.PostDetail.as_view(), name="detail"),
    path("create/", views.PostList.as_view(), name="create"),
]
