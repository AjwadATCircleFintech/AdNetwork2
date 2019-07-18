from django import forms

from .models import Accounts

class PostForm(forms.ModelForm):

    class Meta:
        model = Accounts
        fields = ('email', 'username','password')