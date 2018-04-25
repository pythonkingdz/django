from django.shortcuts import redirect

def log_redirect(request):
    return  redirect('/accounts/login')