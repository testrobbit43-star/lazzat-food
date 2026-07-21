from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'auth'

urlpatterns = [
    # Token-based authentication
    path('token/', obtain_auth_token, name='api_token_auth'),
]
