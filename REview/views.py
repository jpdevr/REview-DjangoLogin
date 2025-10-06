from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm

def home(request):
    return render(request, 'home.html')

def cadastro(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]

            if User.objects.filter(username=username).exists():
                messages.error(request, "Esse nome de usuário já está em uso.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Esse e-mail já está cadastrado.")
            else:
                User.objects.create_user(
                    username=username,
                    email=email,
                    first_name=form.cleaned_data["first_name"],
                    last_name=form.cleaned_data["last_name"],
                    password=form.cleaned_data["password1"],
                )
                messages.success(request, "Cadastro realizado com sucesso! Faça login para continuar.")
                return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "cadastro.html", {"form": form})
