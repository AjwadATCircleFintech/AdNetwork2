from django.shortcuts import render, redirect
from .models import Accounts
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage

#Todo find out why changing space makes the code not work
# Create your views here.

def login(request):

    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            print("This got triggered")
            auth_login(request,user)
            request.session['username'] = user.username
            return redirect('entry')
        else:
            print("No this one got triggered")
            return render(request, 'accounts/login.html')

    else:

        return render(request, 'accounts/login.html')

def signout(request):

    auth_logout(request)

    return redirect('login')

def signup(request): # clean this up later
    # We s shouldn't save users without being able to send them an email link
    # This will definitely cause errors in the future
    # I think we need to deal with email links in a smarter way
    if request.method == 'POST':
        username = request.POST['username']
        fist_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']

        if password == re_password:
           NewUser = Accounts.objects.create_user(username=username, password=password, email=email, first_name=fist_name, last_name=last_name)
           NewUser.is_active = False
           NewUser.save()
           Email_link(request,NewUser)
           return redirect('login')
        else:
            return redirect('signup')

    else:

        return render(request, 'accounts/signup.html')

def recovery(request):

     return render(request,'accounts/recovery.html')



def Email_link(request,newuser):
    #form = SignupForm(request.POST)
    #if form.is_valid():

    current_site = get_current_site(request)
    mail_subject = 'Activate your Circle AdNetwork Account.'
    message = render_to_string('acc_active_email.html', {
            'user': newuser.first_name+" "+newuser.last_name,
            'domain': current_site.domain,
            'uid':  urlsafe_base64_encode(force_bytes(newuser.pk)),#urlsafe_base64_encode(force_bytes(newuser.pk)).decode(),
            'token': account_activation_token.make_token(newuser),
    })
    to_email = newuser.email
    email = EmailMessage(
            mail_subject, message, to=[to_email]
    )

    email.send()

    return redirect('login')

def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Accounts.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        #This also includes logic for if the activation token was already consumed so we don't gotta worry abt this one
        #
        user.is_active = True
        user.save()
        #login(request, user)
        #return redirect('home')
        return redirect('login')
    else:
        return redirect('signup')