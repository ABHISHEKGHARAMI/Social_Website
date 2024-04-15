from django.shortcuts import render
# importing the http response
from django.http import HttpResponse
# importing authenticate for the authenticate and login
from django.contrib.auth import authenticate , login
# importing the form 
from .forms import LoginForm

# Create your views here.

# login view
def user_login(request):
    try:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid :
                cd = form.cleaned_data
                user = authenticate(
                    request,
                    username = cd['username'],
                    password = cd['password']
                )
                if user is not None:
                    if user.is_active:
                        login(user)
                        return HttpResponse("Authenticated Successfully.")
                    else:
                        return HttpResponse("User is inactive.")
                else:
                    return HttpResponse("Invalid Login.")
        else:
            form = LoginForm()
        
        # returning
        return render(
            request,
            'account/login.html',
            {
                'form':form
            }
        )
            
    except Exception as e:
        print(e)
