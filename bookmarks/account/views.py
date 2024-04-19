from django.shortcuts import render
# importing the http response
from django.http import HttpResponse
# importing authenticate for the authenticate and login
from django.contrib.auth import authenticate , login
# importing the form 
from .forms import LoginForm , UserRegistrationForm , UserEditForm , ProfileEditForm

#using the decorator
from django.contrib.auth.decorators import login_required
# importing the model
from .models import Profile

# importing messages
from django.contrib import messages

# Create your views here.

# login view
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form)
        if form.is_valid :
            cd = form.cleaned_data
            user = authenticate(
                    request,
                    username = cd['username'],
                    password = cd['password']
                )
            if user is not None:
                if user.is_active:
                    login(request,user)
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

        
    # super user
    #username = hunter001 password = Abhi1998@
@login_required
def dashboard(request):
    return render(
        request,
        'account/dashboard.html',
        {'section':'dashboard'}
    )


#
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        #print(user_form)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            #saving the new user profile
            Profile.objects.create(user=new_user)
            return render(request,
                'account/register_done.html',
                {
                    'new_user' : new_user
                }
            )
    else:
        user_form = UserRegistrationForm()
    return render(request,
        'account/register.html',
        {
            'user_form' : user_form
        }
    )
    
    
# views for the edit the user and profile
@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance = request.user,
                                 data = request.POST)
        profile_form = ProfileEditForm(instance = request.user,
                                       data = request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,"profile updated successfully.")
        else:
            messages.error(request,"can't update profile.")
    else:
        user_form = UserEditForm(instance = request.user)
        profile_form = ProfileEditForm(instance = request.user.profile)
    
    return render(
        request,
        'account/edit.html',
        {
            'user_form':user_form,
            'profile_form':profile_form
        }
    )