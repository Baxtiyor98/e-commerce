from django.urls import path
from .views import log_out,log_in,register

urlpatterns = [
    path('accounts/login/',log_in,name='login'),
    path('logout/',log_out,name='logout'),
    path('register/',register,name='register'),
]