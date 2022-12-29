from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from .models import User, UserProfile
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('mainapp:join_society')
        else:
            return render(request,'login.html',{'error':'Invalid Credentials'})
    else:
        return render(request,'login.html')
def register(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.create_user(email=email,password=password)
        user.save()
        return redirect('mainapp:login')
    else:
        return render(request,'register.html')
@login_required(login_url='mainapp:login')
def logout(request):
    logout(request)
    return redirect('mainapp:login')
@login_required(login_url='mainapp:login')
def profile(request):
    user=request.user
    profile=UserProfile.objects.get(user=user)
    return render(request,'profile.html',{'profile':profile})
@login_required(login_url='mainapp:login')
def join_society(request):
    user=request.user
    profile=UserProfile.objects.get(user=user)
    if request.method=='POST' and request.is_ajax:
        society=request.POST['society']
        profile.society=society
        profile.save()
        return redirect('mainapp:profile')
    else:
        return render(request,'Join_Society.html')
def gallery(request):
    return render(request,'gallery.html')
def contact(request):
    if request.method=='POST' and request.is_ajax:
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        return JsonResponse(data={'message':'Message Sent Successfully'})
    else:
        return render(request,'contact_us.html')