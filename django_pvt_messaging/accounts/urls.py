from django.urls import path
from . import views

# Passed to urls.py resplatform via include('accounts.urls')
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.logout, name='logout'),
]