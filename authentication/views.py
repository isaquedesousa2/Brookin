from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from django.http import Http404, HttpResponse
from account.models import Account
from .models import User
from django.db.models import Q
from email_validator import validate_email, EmailNotValidError
import json



def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'GET':
        return render(request,'register.html')

def validate_login(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')

        user = User.objects.filter(Q(username=login) | Q(email=login)).first()

        if not user:
            return HttpResponse(json.dumps({'menssage': 'Login ou senha incorretos'}))
        
        user = authenticate(request, username=user.username, password=password)

        if not user:
            return HttpResponse(json.dumps({'menssage': 'Login ou senha incorretos'}))

        login_user(request, user)
        
        return HttpResponse(json.dumps({'status': 'success'}))
    
    raise Http404()


def validate_registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if not username:
            return HttpResponse(json.dumps({'menssage': 'Campo usuário não pode ser vazio!'}))

        try:
            validate_email(email).email
        except EmailNotValidError:
            return HttpResponse(json.dumps({'menssage': 'Digite um email valido!'}))
        
        if len(password) < 6:
            return HttpResponse(json.dumps({'menssage': 'Senha não pode ser menor que 6 caracteres!'}))

        if password != password_confirm:
            return HttpResponse(json.dumps({'menssage': 'Senhas não coencidem'}))

        user_user = User.objects.filter(username=username)
        user_email = User.objects.filter(email=email)

        if user_user:
            return HttpResponse(json.dumps({'menssage': 'Usuário já existe!'}))

        if user_email:
            return HttpResponse(json.dumps({'menssage': 'E-mail já existe!'}))

        user = User.objects.create_user(username=username, email=email, password=password)

        account = Account(user=user)
        account.save()


        return HttpResponse(json.dumps({'status': 'success'}))

    raise Http404()



def logout(request):
    if request.user.is_authenticated:
        logout_user(request)
        return redirect('home')
    raise Http404()



        
            
 