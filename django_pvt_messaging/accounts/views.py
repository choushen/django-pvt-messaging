from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from .forms import CustomUserCreationForm


# Create your views here.
def home(request):
    return render(request, 'accounts/index.html') 


def login(request):

    form = AuthenticationForm() # Create form instance

    if request.method == 'POST':    

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username') # for the sake of AuthenticationForm must scrape username instead of email but username=email
            password = request.POST.get('password') # Get password
            user = authenticate(username=username, password=password) # Authenticate user
            
            if user is not None:
                auth_login(request, user) # Login user using Django's built-in login function
                return redirect('inbox')


    context = {'LoginForm': form} # Pass form to template

    return render(request, 'accounts/login.html', context) 


def registration(request):

    form = CustomUserCreationForm() # Create form instance
    
    if request.method == 'POST':

        form = CustomUserCreationForm(request.POST) # Create form instance

        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return HttpResponse('User creation form is not valid')

    context = {'RegistrationForm': form} # Pass form to template

    return render(request,'accounts/registration.html', context)

def logout(request):
    auth_logout(request) # Logout user using Django's built-in logout function
    return redirect('login')
