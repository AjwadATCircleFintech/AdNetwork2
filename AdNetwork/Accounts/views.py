from django.shortcuts import render, redirect
from .models import Accounts
from django.contrib.auth import authenticate


#Todo find out why changing space makes the code not work
# Create your views here.

def login(request):

    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        print(username)
        print(password)
        user = authenticate(email=username, password=password)
        print(user)
        if user is not None:
            print("This got triggered")
            return render(request, 'accounts/confirmation.html')
        else:
            print("No this one got triggered")
            return render(request, 'accounts/login.html')

    else:

        return render(request, 'accounts/login.html')


def signup(request): # clean this up later

    if request.method == 'POST':
        username = request.POST['username']
        fist_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']

        if password == re_password:
           NewUser = Accounts.objects.create_user(username=username, password=password, email=email, first_name=fist_name, last_name=last_name)
           print(NewUser)
           return redirect('login')
        else:
            return redirect('signup')

    else:

        return render(request, 'accounts/signup.html')





def recovery(request):

    return render(request,'accounts/recovery.html')

def DummyDashBoard(request):

    return None