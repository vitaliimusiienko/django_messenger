from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import SignUpForm, LoginForm
from django.http import HttpResponse

def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            login(request, user)
            
            return redirect('frontpage')
    
    else:
        form = SignUpForm
        
    return render(request, 'core/signup.html', {'form':form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            
            if user is not None:
                
                if user.is_active:
                    
                    login(request, user)
                    
                    return redirect('frontpage')
                
                
                else:
                    return redirect('login')
            else:      
                return redirect('login') 
        
        else:
            return redirect('login')
            
    else:
        form = LoginForm
    
    return render(request, 'core/login.html', {'form':form})

def logout_user(request):
    logout(request)
    
    return redirect('/')
