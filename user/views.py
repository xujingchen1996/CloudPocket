from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .form import RedefinedUserCreationForm, RedefinedUserChangeForm
from .models import commonUser
from django.contrib.auth.decorators import login_required


# Create your views here.


def mainpage(request):
    return render(request, 'home.html')


def loginView(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {'errmsg': '用户名或密码错误!'})
        else:
            login(request, user)
            return redirect('user:mainpage')
    else:
        return render(request, 'login.html')


def logoutView(request):
    logout(request)
    return redirect('user:mainpage')


def registerView(request):
    if request.method == 'POST':
        ucf = RedefinedUserCreationForm(request.POST)
        if ucf.is_valid():
            ucf.save()
            user = authenticate(username=ucf.cleaned_data['username'], password=ucf.cleaned_data['password1'])
            user.email = ucf.cleaned_data['email']
            commonUser(user=user, nickname=ucf.cleaned_data['nickname'], birthday=ucf.cleaned_data['birthday']).save()
            login(request, user)
            return redirect('user:mainpage')
    else:
        ucf = RedefinedUserCreationForm()
    content = {'ucf': ucf}
    return render(request, 'register.html', content)


@login_required(login_url='user:loginView')
def user_center(request):
    content = {'user': request.user}
    return render(request, 'user_center.html', content)


@login_required(login_url='user:loginView')
def edit_profile(request):
    if request.method == 'POST':
        ucf = RedefinedUserChangeForm(request.POST, instance=request.user)
        if ucf.is_valid():
            ucf.save()
            request.user.commonuser.nickname = ucf.cleaned_data['nickname']
            request.user.commonuser.birthday = ucf.cleaned_data['birthday']
            request.user.commonuser.save()
            # commonUser(user=user, nickname=ucf.cleaned_data['nickname'], birthday=ucf.cleaned_data['birthday']).save()
            return redirect('user:user_center')
    else:
        ucf = RedefinedUserChangeForm(instance=request.user)
    content = {'ucf': ucf, 'user': request.user}
    return render(request, 'edit_profile.html', content)


@login_required(login_url='user:loginView')
def change_password(request):
    if request.method == 'POST':
        pcf = PasswordChangeForm(data=request.POST, user=request.user)
        if pcf.is_valid():
            pcf.save()
            # commonUser(user=user, nickname=ucf.cleaned_data['nickname'], birthday=ucf.cleaned_data['birthday']).save()
            return redirect('user:loginView')
    else:
        pcf = PasswordChangeForm(user=request.user)
    content = {'pcf': pcf, 'user': request.user}
    return render(request, 'change_password.html', content)
