from django.shortcuts import render, redirect
from .forms import AccountAuthenticationForm
from django.contrib.auth import login, authenticate, logout, get_user_model
# Create your views here.

def index(request):
    return True

def login_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return redirect("home")
    else: 
        context = {}
        if request.method == 'POST':
            if request.POST.get('usernamelogin'):
                login_form = AccountAuthenticationForm(request.POST)
                if login_form.is_valid():
                    usernamelogin = request.POST['usernamelogin']
                    passwordlogin = request.POST['passwordlogin']
                    user = authenticate(
                        username=usernamelogin, password=passwordlogin) 
                    if user: 
                        login(request, user)
                        return redirect("home")
                else:
                    context['login_form'] = login_form

        return render(request, 'login.html', context)