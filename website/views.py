from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
def home(request):
    #check if user is ligging in 
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #authenticate the user
        user = authenticate(request , username=username, password=password)
        if user is not None:
            login(request , user)
            messages.success(request, 'You are logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('home')
    else:    
      return render(request, 'home.html',{})




def logout_user(request):
    logout(request)
    messages.success(request, 'You are logged out successfully')
    return redirect('home')

def register_user(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authunticate and login
            username = form.cleaned_data.get('username') #take the username entered
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username,password=password)
            login(request,user)
            messages.success(request,f"{user.username} You Have Successfully Registered ")

            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html',{'form':form}) #we passed the form to the html page and use it
    
    return render(request, 'register.html',{'form':form})