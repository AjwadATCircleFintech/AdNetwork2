from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    # path('accounts/login_process',views.login_process, name='loginprocess'), # try to change this, once up fix view functions
    path('accounts/signup', views.signup, name='signup'),
   # path('accounts/confirmation', views.confirmation, name='confirmation'),
    path('accounts/recovery', views.recovery, name='recovery'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^password_reset/$', views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', views.password_reset_complete, name='password_reset_complete'),
]