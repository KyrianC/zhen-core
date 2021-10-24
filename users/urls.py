from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("<str:username>/", views.UserTextList.as_view(), name="texts"),
]
