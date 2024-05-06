from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserDetail

# Create your views here.

@login_required(login_url='/login')
def home(request):
    user_details = UserDetail.objects.get(user=request.user)
    return render(request, "index.html", context={"user": user_details})


def login_view(request):
    if request.user.is_authenticated:
        return redirect(home)
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(username=email).first()
        if user:
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(home)
            else:
                return render(request, "login.html", context={"message": "Invalid Email/Password!"})
        else:
            return render(request, "login.html", context={"message": "User does not exist! Please Sign Up."})
    return render(request, "login.html")


def signup(request):
    if request.user.is_authenticated:
        return redirect(home)
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        ph_no = request.POST['ph_no']
        college = request.POST['college']
        dob = request.POST['dob']
        user = User.objects.create_user(
            username=email, email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()
        user_detail = UserDetail(
            user=user, address=address, ph_no=ph_no, college=college, dob=dob)
        user_detail.save()
        return redirect(login_view)
    return render(request, "signup.html")

def logout_view(request):
    logout(request)
    return redirect(login_view)