from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all() #fetch all the records from the database

    #check if user is logging in 
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
      return render(request, 'home.html',{'records':records}) #we passed the records to the html page and use it




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


def customer_record(request , pk):
    # check if user is logged in
    if request.user.is_authenticated:
        # look up record
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html',{'customer_record':customer_record}) #we passed the record to the html page and use it
    else:
        messages.error(request, 'You are not logged in')
        return redirect('home')


def delete_record(request,pk):
    if request.user.is_authenticated:

        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Record Deleted Successfully')
        return redirect('home')
    else:

        messages.error(request, 'You are not logged in')
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                # save the record to the database
                add_record = form.save()
                messages.success(request,"Record Added...")
                return redirect('home')
        return render(request, 'add_record.html',{'form':form}) #we passed the form to the html page and use it
    else:
        messages.error(request, 'You are not logged in')
        return redirect('home')
    
def update_record(request , pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None , instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record Updated...")
            return redirect('home')
        return render(request, 'update_record.html',{'form':form})
    else:
        messages.error(request, 'You are not logged in')
        return redirect('home')