from django.urls import path

from .endpoint import views, auth_views


urlpatterns = [
    path('', auth_views.google_login),
    path('auth', auth_views.google_auth)
]