from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import RegisterForm

def home(request):
    return render(request, 'home.html')

def cadastro(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password1"],
            )
            # extras (telefone, data nascimento) por enquanto só exibimos no console
            print("Telefone:", form.cleaned_data["phone"])
            print("Nascimento:", form.cleaned_data["birth_date"])

            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "cadastro.html", {"form": form})
