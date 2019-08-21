from django.shortcuts import render, redirect, render_to_response
from Accounts.models import Accounts
from django.contrib.auth.decorators import login_required

# Create your views here.
def entry(request):

    return render(request, 'entry/entry.html')

def entry_home(request):

    return redirect("entry")

def entry_account(request):

    try:
        for key, value in request.session.items():
            print('{} => {}'.format(key, value))
            user_account=Accounts.objects.get(username=request.session['username'])
            print(user_account)
            Account_info={"Username":user_account.username,"First Name":user_account.first_name,"Last Name":user_account.last_name,
                       "Email":user_account.email}

            request.session['account_info']=Account_info

        return render(request, 'entry/entry_account.html',{"items":Account_info})

    except Exception as e:

        print(e)

        print("This one got triggered")

        return render(request, 'entry/entry_account.html')

def entry_account_update(request):




    try:

         return render(request,"entry/entry_account_update.html",{"current_info":request.session['account_info']})

    except Exception as e:

         print(e)
         print("This happened Instead")
         return redirect('entry')

def entry_account_update_save(request):

    return redirect(request,'entry')

def entry_create_company(request):

    return render()
