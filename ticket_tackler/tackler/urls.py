from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    path('view_ticket/<int:ticket_id>/', views.view_ticket, name='view_ticket'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    ]