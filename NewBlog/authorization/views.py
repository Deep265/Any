from django.shortcuts import render,reverse
# Login imports
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Http imports
from django.http import HttpResponse,HttpResponseRedirect
# Models and Forms import
from .forms import User_Form
# Create your views here.
def SignUp(request):
    form = User_Form()
    if request.method == 'POST':
        form = User_Form(request.POST)
        if form.is_valid:
            form.save()
    return render(request,'authorization/signup.html',{'form':form})

def LoginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('blog:post_list'))
            else:
                return HttpResponse('User is not active')
        else:
            return HttpResponse('User Does not exists')
    return render(request,'authorization/login.html')

@login_required
def LogoutUser(request):
    logout(request)
    return HttpResponseRedirect('/authorize/login/')



