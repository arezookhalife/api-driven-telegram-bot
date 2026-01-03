from django.urls import path
from .views import reply_api

urlpatterns = [
    path("reply/", reply_api, name="reply_api"),
]
