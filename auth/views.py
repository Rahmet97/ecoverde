from django.contrib.auth import login, logout
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Choose a username', 'autocomplete': 'username',
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'you@example.com', 'autocomplete': 'email',
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'At least 8 characters', 'autocomplete': 'new-password',
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Repeat your password', 'autocomplete': 'new-password',
        })


def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    form.fields['username'].widget.attrs.update({
        'placeholder': 'Your username', 'autocomplete': 'username',
    })
    form.fields['password'].widget.attrs.update({
        'placeholder': 'Your password', 'autocomplete': 'current-password',
    })
    if request.method == 'POST' and form.is_valid():
        login(request, form.get_user())
        return redirect('home')
    return render(request, 'login.html', {'form': form})


def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')
