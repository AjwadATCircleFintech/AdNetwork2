from django.shortcuts import render
from django.contrib.auth import authenticate


#Todo find out why changing space makes the code not work
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
        print("This got triggered")
        return render(request,'accounts/confirmation.html')
    else:
        print("No this one got triggered")
        return render(request,'accounts/login.html')

def recovery(request):

    return render(request,'accounts/recovery.html')

def DummyDashBoard(request):

    return None