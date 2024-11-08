from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import RegisterUserForm





def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password=password)
        if user is not None:
            
            login(request, user=user)
            # redirect to success page
            return redirect('contact-list')
        else:
            messages.success(request,  "There was an error logging in. Try Again...")
            # Return invalid login error message
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})
 
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("login")   
    
    
def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user =  authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, "Registration Successful")
            return redirect("contact-list")
        
    else:
        form = RegisterUserForm()
            
        
        
        
        
    return render(request, 'authenticate/register.html',  {'form': form})
        
