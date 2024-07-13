from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    path('inbox/chat/<int:user_id>/', views.chat, name='chat'),
    path('send_message/<int:user_id>/', views.send_message, name='send_message'),
    path('fetch_notifications/', views.fetch_notifications, name='fetch_notifications'),
]
