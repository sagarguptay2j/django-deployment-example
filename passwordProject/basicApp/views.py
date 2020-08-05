from django.shortcuts import render
from basicApp.forms import UserForm,UserProfileInfoForm

from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'basicApp/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HtttpResponse("User is not active")
        else:
            return HtttpResponse("Invalid Login Details")

    else:
        return render(request,'basicApp/login.html')



def registration(request):
    registered = False

    if request.method == 'POST':
        userForm = UserForm(data = request.POST)
        profileForm = UserProfileInfoForm(data = request.POST)

        if userForm.is_valid() and profileForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()

            profile = profileForm.save(commit=False)
            profile.user = user

            if 'profilePic' in request.FILES:
                profile.profilePic = request.FILES['profilePic']

            profile.save()

            registered = True

        else:
            print(userForm.errors,profileForm.errors)
    else:
        userForm = UserForm
        profileForm = UserProfileInfoForm

    return render(request,'basicApp/registration.html',{'userForm':userForm,'profileForm':profileForm,'registered':registered})
