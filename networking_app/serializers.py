from rest_framework import serializers, viewsets
from .models import NetworkingUserModel

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkingUserModel
        fields = '__all__'

class PersonViewSet(viewsets.ModelViewSet):
    queryset = NetworkingUserModel.objects.all()
    serializer_class = PersonSerializer
