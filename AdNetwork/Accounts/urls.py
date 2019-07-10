from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/confirmation', views.confirmation, name='confirmation'),
    path('accounts/recovery', views.recovery, name='recovery'),
]