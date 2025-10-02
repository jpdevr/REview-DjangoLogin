from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label="Senha", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Senha", widget=forms.PasswordInput)
    phone = forms.CharField(label="Telefone", max_length=20)
    birth_date = forms.DateField(label="Data de Nascimento", widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = User
        fields = ["username", "email"]

    def clean_password2(self):
        p1 = self.cleaned_data.get("password1")
        p2 = self.cleaned_data.get("password2")
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("As senhas não coincidem")
        return p2
