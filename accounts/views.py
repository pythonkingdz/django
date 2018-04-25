from django.shortcuts import render ,redirect
from .models import Post
from .forms import RegistrationForm ,EditProfile
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


def home(request):
    posts = Post.objects.all()
    datas = {'posts': posts}
    return render(request, 'accounts/index.html', datas)



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else:
        form = RegistrationForm()

        args={'form':form}
        return render(request,'accounts/reg_form.html',args)



def profile(request):
    args = {'user':request.user}
    return render(request ,'accounts/profile_user.html' , args)

def technology(request):

    return render(request ,'accounts/technology.html')

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfile(request.POST ,instance=request.user)

        if form.is_valid():
            form.save()

            return redirect('/accounts/profile')
    else:
        form = EditProfile(instance=request.user)

        args={'form':form}
        return render(request,'accounts/edit_profile.html',args)


def change_password(request):
    if request.method=='POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/accounts/profile')
        else:
            return  redirect('/accounts/change_password')

    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request,'accounts/chnage_pass.html',args)

