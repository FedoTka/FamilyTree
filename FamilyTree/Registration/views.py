from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import UserForm
from django.views.generic import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import BaseUserManager
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
import jwt
from rest_framework.views import Response
from .models import User
from .serializers import UserSerialiezer

class Register(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'Registration/registration_form.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        access_token = request.auth
        access_token = str(access_token).encode('utf-8')
        decode = jwt.decode(access_token, options={"verify_signature": False})
        user_profile = User.objects.get(id=decode['user_id'])
        serializer = UserSerialiezer(user_profile)
        return Response(serializer.data)

