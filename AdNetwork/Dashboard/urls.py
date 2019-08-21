from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('entry/',views.entry, name='entry'),
    path('entry/account',views.entry_account, name='entry_account'),
    path('entry/account_update',views.entry_account_update, name='entry_account_update'),
    path('entry/account_update_save',views.entry_account_update_save, name='entry_account_update_save')
]