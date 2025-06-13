from django.urls import path
from .views import (
    ProjectListCreateView,
    HeroDetailView,
    AboutDetailView,
    CommunityDetailView,
    ContactUsDetailView,
    ProjectRetrieveView
)

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='projects'),
    path('projects/<int:pk>', ProjectRetrieveView.as_view(), name='projects'),
    path('hero/', HeroDetailView.as_view(), name='hero'),
    path('hero/<int:pk>/', HeroDetailView.as_view(), name='hero-detail'),
    path('about/<int:pk>/', AboutDetailView.as_view(), name='about'),
    path('community/<int:pk>/', CommunityDetailView.as_view(), name='community'),
    path('contact/<int:pk>/', ContactUsDetailView.as_view(), name='contact'),
]
