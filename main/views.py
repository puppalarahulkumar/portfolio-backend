from rest_framework import generics
from .models import ProjectModel, HeroModel, AboutSectionModel, CommunityModel, ContactUsModel
from .serializers import (
    ProjectSerializer,
    HeroSerializer,
    AboutSectionSerializer,
    CommunitySerializer,
    ContactUsSerializer,
)

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializer

class ProjectRetrieveView(generics.RetrieveAPIView):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'pk'  # default, but made explicit

# Hero section (Only one object expected)
class HeroDetailView(generics.RetrieveAPIView):
    queryset = HeroModel.objects.all()
    serializer_class = HeroSerializer

    def get_object(self):
        return HeroModel.objects.first()  # Assuming only 1 row

# About section
class AboutDetailView(generics.RetrieveAPIView):
    queryset = AboutSectionModel.objects.all()
    serializer_class = AboutSectionSerializer

    def get_object(self):
        return AboutSectionModel.objects.first()

# Community section
class CommunityDetailView(generics.RetrieveAPIView):
    queryset = CommunityModel.objects.all()
    serializer_class = CommunitySerializer

    def get_object(self):
        return CommunityModel.objects.first()

# Contact us section
class ContactUsDetailView(generics.RetrieveAPIView):
    queryset = ContactUsModel.objects.all()
    serializer_class = ContactUsSerializer

    def get_object(self):
        return ContactUsModel.objects.first()
