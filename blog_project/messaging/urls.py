from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    path('message/<int:pk>/', views.view_message, name='view_message'),
    path('send/', views.send_message, name='send_message'),
    path('send_message/', views.send_message, name='send_message'),
    path('message/<int:pk>/', views.view_message, name='view_message'),
    path('message/<int:pk>/delete/', views.delete_message, name='delete_message'),

]
