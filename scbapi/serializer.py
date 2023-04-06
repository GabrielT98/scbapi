from rest_framework import serializers
from .models import User, Barraginha

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barraginha
        fields = '__all__'