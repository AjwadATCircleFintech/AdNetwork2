from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('accounts/login_process',views.login_process, name='loginprocess'), # try to change this, once up fix view functions
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/confirmation', views.confirmation, name='confirmation'),
    path('accounts/recovery', views.recovery, name='recovery'),
]