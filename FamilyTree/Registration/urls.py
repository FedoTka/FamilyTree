from django.urls import path

from .views import *

urlpatterns = [
    path('', Register.as_view(), name='registration'),
]