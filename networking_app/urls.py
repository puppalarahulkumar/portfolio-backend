from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import NetworkingUserView


urlpatterns = [
    path("user/", NetworkingUserView.as_view(), name="networking_users"),
]