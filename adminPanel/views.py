from django.shortcuts import render, redirect
from .forms import AccountAuthenticationForm
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Auth
# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        sensor = data['sensor']
        value = data['value']
        
        if sensor == 'gas':
            gas_value = value
            print(gas_value)
        elif sensor == 'photo':
            photo_value = value
        elif sensor == 'infared':
            infa_value = value
        try:
            print(gas_value)
        except:
            gas_value = 0
        try:
            print(photo_value)
        except:
            photo_value = 0
        try:
            print(infa_value)
        except:
            infa_value = 0    
        
        context = {
            'gas_value': gas_value,
            'photo_value': photo_value,
            'infa_value': infa_value,
        }

        return JsonResponse(context)
        
    try:
        print(gas_value)
    except:
        gas_value = 0
    try:
        print(photo_value)
    except:
        photo_value = 0
    try:
        print(infa_value)
    except:
        infa_value = 0    
    
    context = {
        'gas_value': gas_value,
        'photo_value': photo_value,
        'infa_value': infa_value,
    }
    return render(request, 'index.html', context)

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
    
@csrf_exempt
def secondAuth(request):
    accounts = Auth.objects.all()
    if request.method == 'POST':
        data = json.loads(request.body)
        for i in len(accounts):
            if i.auth_id == data['auth_id']:
                return HttpResponse(i.belong_to)
            
@csrf_exempt
def receiveData(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
    return HttpResponse('Data was received')