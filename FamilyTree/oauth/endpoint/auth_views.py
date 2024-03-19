from django.shortcuts import render
from rest_framework.views import Response
from rest_framework.decorators import api_view
from .. import serializers
from rest_framework.exceptions import AuthenticationFailed
from ..services import google
def google_login(request):
    """Страница входа через google"""

    return render(request, 'oauth/google_login.html')



@api_view(["POST"])
def google_auth(request):
    """Подтверждение авторизации через Google"""
    google_data = serializers.GoogleAuth(data=request.data)
    if google_data.is_valid():
        return Response(google.check_google_auth(google_data))
    else:
        return AuthenticationFailed(code=403, detail='Bad data Google')
