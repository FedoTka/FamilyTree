from rest_framework.permissions import IsAuthenticated
from  rest_framework.views import APIView
from .models import User
from rest_framework.serializers import ModelSerializer


class UserSerialiezer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
