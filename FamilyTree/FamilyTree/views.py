from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_view(request):
    return HttpResponse({'message':'This is protected view'})


class CustomLoginView(LoginView):
    template_name = 'login_form.html'
    redirect_authenticated_user = True
    def get_success_url(self):
        return '/'

def home_page(request):
    return render(request, 'home.html')