from django.shortcuts import render
from django.contrib.auth import authenticate

# Create your views here.
def login(request):
    # Confirm with authenticate

    return render(request, 'accounts/login.html')


def signup(request):
    return render(request, 'accounts/signup.html')

def confirmation(request):
    username = request.POST['Username']
    password = request.POST['Password']
    print(username)
    print(password)
    user = authenticate(username=username,password=password)
    print(user)
    if user is not None:
        return render(request,'accounts/confirmation.html')
    else:
        return render(request,'accounts/login.html')

def recovery(request):

    return render(request,'accounts/recovery.html')

def DummyDashBoard(request):

    return None