"""
URL configuration for crypto_alerts project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from alerts import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('alerts/create/', views.create_alert, name='create_alert'),
    path('alerts/', views.list_alerts, name='list_alerts'),
    path('alerts/<int:alert_id>/', views.show_alert, name='show_alert'),
    path('alerts/<int:alert_id>/update/', views.update_alert, name='update_alert'),
    path('alerts/<int:alert_id>/delete/', views.delete_alert, name='delete_alert'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
