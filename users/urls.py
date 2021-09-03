from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("<int:pk>/", views.UserTextList.as_view(), name="texts"),
]
