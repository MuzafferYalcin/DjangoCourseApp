from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from account.forms import LoginUserForm, NewUserForm, UserPasswordChangeForm


def user_login(request):
    if request.method == 'POST':
        form = LoginUserForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request,username = username, password = password )

            if user is not None:
                login(request,user)
                return redirect("kurs")
            else:
                return render(request, 'account/login.html', {"form":form})
        else:
            return render(request, 'account/login.html', {"form":form})
    else:
        form = LoginUserForm()
        return render(request, 'account/login.html',{"form":form})
 

def user_register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return render(request, "account/register.html", {"form":form})
    else:
        form = NewUserForm()
        return render(request, "account/register.html", {"form":form})


def change_password(request):
    if request.method == 'POST':
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            return redirect('change_password')
        else:
            return render(request, 'account/change-password.html', {'form': form} )

    form = UserPasswordChangeForm(request.user)
    return render(request, 'account/change-password.html', {'form': form} )


def user_logout(request):
    logout(request)
    return redirect('kurs')

