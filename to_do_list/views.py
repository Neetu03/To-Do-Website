from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django. contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def home(request):
    return render(request,"home.html")
def login_page(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request, "Invalid username or password")
            return redirect('/login/')
        else:
            login(request, user)  # Corrected here
            return redirect('/to-do/')
    return render(request, "login.html")
def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        u=User.objects.filter(username=username)
        if u.exists():
            messages.info(request,"User Already exists")
            return redirect('/register/')
        u=User.objects.create(username=username)
        u.set_password(password)
        u.save()

    messages.info(request,"account created successfully")
    return render(request,'register.html')

def my_to_do(request):
    if request.method=="POST":
        data=request.POST
        Task=data.get('to_do_task')
        Description=data.get('to_do_description')
        m=task(Task=Task,Description=Description)
        m.save()
        return redirect('/to-do/')
    queryset=task.objects.all()
    return render(request,'index.html',{'queryset':queryset})
    
def edit_task(request,id):
    task_to_do=task.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        Task=data.get('to_do_task')
        Description=data.get('to_do_description')
        task_to_do.Task=Task
        task_to_do.Description=Description
        task_to_do.save()
        messages.success(request, "Task Updated!")
        return redirect('/to-do/')
        
    context={'task_to_do':task_to_do}
    return render(request,"edit.html",context)

def delete_task(request,id):
    queryset=task.objects.get(id=id)
    queryset.delete()
    return redirect('/to-do/')
