from django.contrib import admin
from django.urls import path, include
from .views import home_page
from django.contrib.auth.views import LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from Registration.views import UserProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('registration/', include('Registration.urls')),
    path('api/v1/profile', UserProfileView.as_view(), name='profile'),
    path('login/', include('Authorization.urls')),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('oauth/', include('oauth.urls')),
]
