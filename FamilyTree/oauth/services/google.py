from rest_framework.exceptions import AuthenticationFailed
from .. import serializers
from google.oauth2 import id_token
from google.auth.transport import requests
from Registration.models import User
from rest_framework import status
from rest_framework.response import Response
import jwt
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


def check_google_auth(google_user: serializers.GoogleAuth):
    try:
        id_token.verify_oauth2_token(google_user.data['token'], requests.Request())
        token = google_user.data['token']
        decode_token = jwt.decode(token, options={"verify_signature": False})
    except ValueError as Ex:
       raise AuthenticationFailed(code=403, detail='Bad token Google')

    email = decode_token['email']
    name = decode_token['given_name']
    second_name = decode_token['family_name']

    user, _ = User.objects.get_or_create(email=email, nickname=email, name=name, second_name=second_name)

    # Генерируем токены
    refresh_token = RefreshToken.for_user(user)
    access_token = refresh_token.access_token

    return {'refresh_token': str(refresh_token),
            'access_token': str(access_token)}