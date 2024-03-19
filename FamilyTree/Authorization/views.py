from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import View
from Authorization.forms import LoginForm
from rest_framework.views import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView


class Login(TokenObtainPairView):
    def get(self, request):
        form = LoginForm()
        return render(request, 'Authorization/login.html', {'form': form})
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response
