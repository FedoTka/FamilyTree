from rest_framework.exceptions import AuthenticationFailed
from .. import serializers
from google.oauth2 import id_token
from google.auth.transport import requests
from Registration.models import User
import jwt



def check_google_auth(google_user: serializers.GoogleAuth):
    try:
        id_token.verify_oauth2_token(google_user.data['token'], requests.Request())
        token = google_user.data['token']
        decode_token = jwt.decode(token, options={"verify_signature": False})
    except ValueError as Ex:
       raise AuthenticationFailed(code=403, detail='Bad token Google')

    email = decode_token['email']
    name = decode_token['name']

    user, _ = User.objects.get_or_create(email=email)


    return {'user_id': 3,
            'access_token': token}