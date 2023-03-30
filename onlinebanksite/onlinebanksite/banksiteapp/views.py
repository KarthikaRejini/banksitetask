from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username is exist ')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username,password=password)

                user.set_password(password)
                user.save()
                print("success")
                return redirect('login_user')
        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(register)
    else:

        print("no post method")
    return render(request, 'register.html')
def login_user(request):
    if request.method == 'POST':
        username =request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('new_form')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')

    else:
        return render(request, 'login.html')
def new_form(request):

    return render(request, 'new.html')



def form_user(request):

    return render(request,'form.html')

def logout_user(request):
    auth.logout(request)
    return redirect('logout_user')
def submitlink(request):

    messages.info(request, 'succesfully saved')

    return render(request,'submitlink.html')
